const net = require('net');
const { calculateCRC, toWord } = require('./CRC32/CRCAlgorithm');


const HOST = '127.0.0.1';
const PORT = 65123;

const server = net.createServer((socket) => {
    console.log(`Conexion Entrante del proceso ${socket.remoteAddress}:${socket.remotePort}`);
    
    socket.on('data', (data) => {
        // console.log(`Recibido: \n${data}`);

        let newData = JSON.parse(data);
        // Para un comportamiento de "echo", podrías enviar de vuelta los datos con:
        // socket.write(data);
        
        // decodificacion = calculateCRC("110110010011001101010010101110111110011")

        // CAPA DE ENLACE ---------verificar integridad/corregir--------------------------
        
        if (newData.type === 0) {
            //Hamming
            console.log('No se han detectado errores. \nTrama recibida:',message.slice(0, polinomio.length))
        } else if (newData.type === 1) {
            //CRC
            decodificated_message = []
            for (let value of newData.message) {
                decodificacion = calculateCRC(value)
                decodificated_message.push(decodificacion)
            }
            console.log('decodificacion',decodificated_message)
        }

        //-----------------------------------------------------
         // CAPA DE PRESENTACION ---------decodificar el mensaje (pasarlo a letras)--------------------------
        let wordmessge = []
        for (let char of decodificated_message) {
            wordmessge.push(toWord(char))
        }
        
        //-----------------------------------------------------
        
        // CAPA DE APLICACION ---------mostrar el mensaje--------------------------
        console.log("Mensaje convertido",wordmessge)

        //-----------------------------------------------------
        
    });

    socket.on('end', () => {
        console.log(`Desconexión del proceso ${socket.remoteAddress}:${socket.remotePort}`);
    });

    socket.on('error', (err) => {
        console.error(`Error en la conexión con ${socket.remoteAddress}:${socket.remotePort}: ${err.message}`);
    });
});

server.listen(PORT, HOST, () => {
    console.log(`Servidor escuchando en ${HOST}:${PORT}`);
});

server.on('error', (err) => {
    console.error(`Error del servidor: ${err.message}`);
});
