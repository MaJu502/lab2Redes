const fs = require('fs');

function DivideXOR(trama, polinomio) {
    // Esta función toma dos cadenas binarias como parámetros de entrada y calcula 
    // su resultado XOR (O exclusivo). La operación XOR se realiza en los bits correspondientes 
    // de las dos cadenas binarias, resultando en una nueva cadena binaria que representa la 
    // operación lógica XOR entre las dos entradas.

    var result = [];
    for (var i = 0; i < polinomio.length; i++) {
        result.push(String(Number(trama[i]) ^ Number(polinomio[i])));
    }

    return result;
}

function CRC32(input, pol) {
    // Definición de valores
    var polinomio = Array.from(pol);
    var trama = Array.from(input);

    // Inicializamos con los primeros n (longitud del polinomio) bits de la trama original
    var result = trama.slice(0, polinomio.length);

    // Repetimos por cada bit extra de la trama
    for (var i = 0; i < trama.length - polinomio.length + 1; i++) {
        if (result[0] === '1') {
            result = DivideXOR(result, polinomio);
        } else {
            result = DivideXOR(result, Array(polinomio.length).fill('0'));
        }
        // eliminamos el primer bit del resultado.
        result.shift();
        // Si todavía hay bits por baja en la trama original. 
        if (i !== (trama.length - polinomio.length + 1) - 1) {
            // bajamos el bit siguiente de la trama original.
            result.push(trama[(polinomio.length + i)]);
        }
    }

    return result;
}

function generateBinaryStrings(n, message, polinomio) {
    var result = [];
    var max = Math.pow(2, n);
  
    for (var i = 0; i < max; i++) {
        var bin = i.toString(2);
        // Añadimos ceros a la izquierda si es necesario para alcanzar la longitud n
        bin = '1'.repeat(n - bin.length) + bin;
        console.log(bin)

        var resultado = CRC32(bin, polinomio).join('')

        if (resultado === '0'.repeat(resultado.length) && bin != message) {
            console.log('utiliza la cadena',bin)
            console.log('No se han detectado errores.')
            break
        } else {
            // console.log('Se han detectado errores. Trama descartada')
        }

    }
  
}



fs.readFile('./CRC32/message.txt', 'utf8', (err, message) => {
        if (err) {
            console.error('Ocurrió un error al leer el archivo message.txt:', err);
            return;
        }

        fs.readFile('./CRC32/polinomio.txt', 'utf8', (err, polinomio) => {
            if (err) {
                console.error('Ocurrió un error al recuperar el polinomio:', err);
                return;
            }
  
      // Calculamos los bits con el algoritmo
        var resultado = CRC32(message, polinomio).join('');

        if (resultado === '0'.repeat(resultado.length)) {
            console.log('No se han detectado errores. \nTrama recibida:',message.slice(0, polinomio.length))
        } else {
            console.log('Se han detectado errores. Trama descartada')
        }

        // generateBinaryStrings(message.length+1, message, polinomio)

    });
});
  