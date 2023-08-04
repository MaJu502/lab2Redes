
const fs = require('fs');



// Ruta del archivo
const rutaArchivo = './message.txt';

function soloHayCeros(cadenaBinaria) {
    for (let i = 0; i < cadenaBinaria.length; i++) {
        if (cadenaBinaria[i] !== '0') {
            return false; // Si encontramos algún caracter diferente de '0', retornamos false
        }
    }
    return true; // Si todos los caracteres son '0', retornamos true
}

function XOR(b1, b2) {
    const result = b1 !== b2 ? '1' : '0';
    return result;
}

function CRC32(trama, polynomial) {


    // Trama + n 0s
    let tempCode = trama;

    // Trama - bits de inicio
    let new_t = tempCode.slice(polynomial.length);

    while (true) {
        let result = '';
        // console.log(tempCode);
        // console.log(polynomial);
        // console.log('----------');

        for (let i = 0; i < polynomial.length; i++) {
            result += XOR(polynomial[i], tempCode[i]);
        }

        // console.log(result, '\n');

        // Eliminamos los 0 antes del primer 1
        // Ej. 010 -> 10
        let temp_result = result;
        result = result.replace(/^0+/, '');

        if (result === '' && !new_t.includes('1')) {
            return temp_result;
        }

        // Calculamos el desplazamientos de bits que hay que bajar de la trama original
        let temp = '';
        const lenNew = polynomial.length - result.length;

        if (new_t.length >= lenNew) {
            // Por cada desplazamiento que hubo
            for (let i = 0; i < lenNew; i++) {
                // Sacamos un bit de la trama original
                temp += new_t.charAt(0);
                // Eliminamos ese bit de la trama original
                new_t = new_t.slice(1);
            }
        } else {
            return temp_result.slice(-(polynomial.length - 1));
        }

        tempCode = result + temp;
    }
}


let polynomial = "100000100110000010001110110110111"
// polynomial = '1001'
// Leer el archivo
fs.readFile(rutaArchivo, 'utf8', (err, data) => {
    if (err) {
        console.error('Error al leer el archivo:', err);
    } else {
        console.log('mensaje', data)
        result = CRC32(data, polynomial)
        if (soloHayCeros(result)){
            console.log('No se han detectado errores. \nTrama ->',data)
        } else {
            console.log('Se han detectado errores. Trama descartada')
        }
    }
});
