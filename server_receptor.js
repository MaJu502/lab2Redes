const net = require('net');
const { calculateCRC, toWord } = require('./CRC32/CRCAlgorithm');
const { decodeHamming } = require('./Hamming/receptorHam');


const HOST = '127.0.0.1';
const PORT = 65123;

const server = net.createServer((socket) => {
    console.log(`Conexion Entrante del proceso ${socket.remoteAddress}:${socket.remotePort}`);
    let error_detection = 0
    let mensajeResHam; 
    let contadorErroresHam = 0;
    let contadorCorreccionesHam = 0;
    let mensajeOrgienHam;
    let iters = 0;
    
    socket.on('data', (data) => {
        // console.log(`Recibido: \n${data}`);

        let newData = JSON.parse(data);
        // Para un comportamiento de "echo", podrías enviar de vuelta los datos con:
        // socket.write(data);
        
        // decodificacion = calculateCRC("110110010011001101010010101110111110011")

        // CAPA DE ENLACE ---------verificar integridad/corregir--------------------------
        let validateIntegrity = true
        if (newData.type === 0) {
            //Hamming
            iters += 1;
            decodificated_message = []
            for (let value of newData.message) {
                resHamming = decodeHamming(value)
                mensajeResHam = resHamming[0]
                contadorErroresHam += resHamming[1]
                decodificated_message.push(mensajeResHam)
            }
            mensajeOrgienHam = newData.original
            console.log('mensaje original -> ',mensajeOrgienHam)
            console.log('decodificacion',decodificated_message)
            console.log('Cantidad de errores -> ', contadorErroresHam)
        } else if (newData.type === 1) {
            //CRC
            
            decodificated_message = []
            for (let value of newData.message) {
                [decodificacion,newval] = calculateCRC(value)
                decodificated_message.push(decodificacion) // <--- Lista con los caracteres binarios (sin los bits de paridad)
                if (newval==false){
                    validateIntegrity = false
                }
            }
        }

        //-----------------------------------------------------
         // CAPA DE PRESENTACION ---------decodificar el mensaje (pasarlo a letras)--------------------------
        let wordmessge = toWord(decodificated_message) // <--- Toma la lista, convierte cada caracter binario a ASCII y devuelve la lista ahora con valores ascii
        
        //-----------------------------------------------------

        // verificar mensaje hamming

        if (mensajeOrgienHam  !== wordmessge) {
            contadorCorreccionesHam += 1
        }
        
        // CAPA DE APLICACION ---------mostrar el mensaje--------------------------
        console.log("Mensaje recibido desde el emisor:\n>",wordmessge)
        console.log("Cantidad de recibidos con o sin correcciones malos -> ", contadorCorreccionesHam)
        console.log("cantidad de iteraciones -> ", iters)
        // console.log(validateIntegrity)
        if (!validateIntegrity) {
            error_detection += 1
        }

        //-----------------------------------------------------
        
    });

    

    socket.on('end', () => {
        console.log("errores detectados",error_detection)
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
