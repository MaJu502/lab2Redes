const net = require('net');

const HOST = '127.0.0.1';
const PORT = 65123;

const server = net.createServer((socket) => {
    console.log(`Conexion Entrante del proceso ${socket.remoteAddress}:${socket.remotePort}`);
    
    socket.on('data', (data) => {
        console.log(`Recibido: \n${data}`);
        // Para un comportamiento de "echo", podrías enviar de vuelta los datos con:
        // socket.write(data);
        
        // decodificacion = 

        // CAPA DE ENLACE ---------verificar integridad/corregir--------------------------
        
        // si type es 0
        //     decodificacion = hamming(data)
        // si type es 1
        //     decodificacion = crc(data)

        //-----------------------------------------------------
         // CAPA DE PRESENTACION ---------decodificar el mensaje (pasarlo a letras)--------------------------
        


        //-----------------------------------------------------

         // CAPA DE APLICACION ---------mostrar el mensaje--------------------------


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
