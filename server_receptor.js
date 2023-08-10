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
        let validateIntegrity = true
        if (newData.type === 0) {
            
            //HAMMINH

            //YOUR CODE HERE

            console.log('No se han detectado errores. \nTrama recibida:',message.slice(0, polinomio.length))

        } else if (newData.type === 1) {
            //CRC
            
            decodificated_message = []
            for (let value of newData.message) {
                [decodificacion,validateIntegrity] = calculateCRC(value)
                decodificated_message.push(decodificacion) // <--- Lista con los caracteres binarios (sin los bits de paridad)
                if (validateIntegrity==false){
                    validateIntegrity = false
                }
            }
        }

        //-----------------------------------------------------
         // CAPA DE PRESENTACION ---------decodificar el mensaje (pasarlo a letras)--------------------------
        let wordmessge = toWord(decodificated_message) // <--- Toma la lista, convierte cada caracter binario a ASCII y devuelve la lista ahora con valores ascii
        
        //-----------------------------------------------------
        
        // CAPA DE APLICACION ---------mostrar el mensaje--------------------------
        console.log("Mensaje recibido desde el emisor:\n>",wordmessge)
        console.log(validateIntegrity)

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
