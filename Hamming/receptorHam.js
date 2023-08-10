const fs = require('fs');

// Función para convertir un arreglo de cadenas de números a un arreglo de arreglos de enteros
function convertirArregloEntero(arregloCadenas) {
    return arregloCadenas.map(cadena => cadena.split('').map(Number));
}

// Función para contar la cantidad de 1's en un arreglo
function contarUnos(arreglo) {
    return arreglo.reduce((contador, elemento) => contador + elemento, 0);
}

// Función para obtener el contenido por código
function obtenerContenidoDecodificado(contenido, arregloCodesEnteros) {
    return arregloCodesEnteros.map(codigo => codigo.map(j => contenido[j]));
}

// Función para verificar si un array contiene únicamente 0's
function contieneSoloCeros(array) {
    return array.every(elemento => elemento === 0);
}

function toWordedHam(x) {
    var binary_list = x; // arreglo
    var char_list = [];

    for (var i = 0; i < binary_list.length; i++) {
        var binary_code = binary_list[i];
        var decimal_value = parseInt(binary_code, 2);  // Convierte el código binario a decimal
        char_list.push(String.fromCharCode(decimal_value));  // Convierte el valor decimal a un caracter y agrega a la lista
    }

    return char_list.join('');  // Une la lista de caracteres en una cadena
}


function decodeHamming(binaryinfo) {
    const arregloMensajes = binaryinfo[0];
    const arregloCodes = binaryinfo[1];

    const arregloMensajesEnteros = convertirArregloEntero(arregloMensajes);

    const arregloMensajesInvertidos = arregloMensajesEnteros.map(arreglo => arreglo.reverse());

    const arregloCodesEnteros = convertirArregloEntero(arregloCodes);
    const decimalesporMensaje = [];

    // Descodificar
    for (let i = 0; i < arregloMensajesInvertidos.length; i++) {
        const resultado_paridad = new Array(arregloCodesEnteros.length);
        const contenido = arregloMensajesInvertidos[i];
        const contenidoPorCodigo = obtenerContenidoDecodificado(contenido, arregloCodesEnteros);

        for (let j = 0; j < contenidoPorCodigo.length; j++) {
            const codigo = contenidoPorCodigo[j];
            const cantidadUnos = contarUnos(codigo);
            const cantidadCeros = codigo.length - cantidadUnos;

            // Verificar si hay par o impar en la cantidad de 1's y 0's
            if (cantidadUnos % 2 === 0 && cantidadCeros % 2 === 0) {
                resultado_paridad[j] = 0;
            } else {
                resultado_paridad[j] = 1;
            }
        }

        const resultado = resultado_paridad.join('');
        const gg = parseInt(resultado, 2);
        decimalesporMensaje[i] = gg;
    }

    // Buscar el error
    if (contieneSoloCeros(decimalesporMensaje)) {
        console.log('\n-------------------------------------------------------------------\n');
        console.log('Todo bien, el mensaje recibido exitosamente es:');
        const temp = [];

        for (const x of arregloMensajes) {
            const mensajeInvertido = x.split('').reverse().join('');
            temp.push(mensajeInvertido);
        }


        for (let i = 0; i < temp.length; i++) {
            const tempArray = temp[i].split(''); // Convierte la cadena en un arreglo
            tempArray.splice(3, 1); // Borra la posición 3
            tempArray.splice(1, 1); // Borra la posición 1
            tempArray.splice(0, 1); // Borra la posición 0
            temp[i] = tempArray.join(''); // Convierte el arreglo en una cadena nuevamente
        }

        const arregloAgrupado = temp.map(arreglo => arreglo.split('').join(''));

        const resultadoFinal = arregloAgrupado.join('');
        console.log("------> FINAL FINAL FINAL FIANAAAAAAAAAAAL");
        console.log(resultadoFinal);

        console.log(`  Mensaje final -> ${resultadoFinal}`);
        console.log('\n-------------------------------------------------------------------\n');
        return resultadoFinal
    } else {
        for (const x of arregloMensajes) {
            console.log(`  Mensaje original -> ${x}`);
        }
        for (let i = 0; i < arregloMensajesInvertidos.length; i++) {
            const elemento = arregloMensajesInvertidos[i];
            const indi = decimalesporMensaje[i];
            if (indi > 0 && indi < elemento.length) {
                const hh = elemento[indi - 1];
                const nuevo_num = hh === 0 ? 1 : 0;
                console.log(`     --> Se ha cambiado el bit erroneo ${hh} en el indice ${indi} por ${nuevo_num} para corregir el mensaje.`);
                elemento[indi - 1] = nuevo_num;
                arregloMensajesInvertidos[i] = elemento;
            } else if (indi === 0) {
                // No se hace nada
            } else {
                console.log(`Error: el índice ${i} está fuera del rango del arregloMensajes.`);
            }
        }

        const arregloMensajesDesinvertidos = arregloMensajesInvertidos.map(arreglo => arreglo.reverse());

        for (let i = 0; i < arregloMensajesDesinvertidos.length; i++) {
            arregloMensajesDesinvertidos[i].splice(3, 1); // Borra la posición 3
            arregloMensajesDesinvertidos[i].splice(1, 1); // Borra la posición 1
            arregloMensajesDesinvertidos[i].splice(0, 1); // Borra la posición 0
        }
          
        const arregloAgrupado = arregloMensajesDesinvertidos.map(arreglo => arreglo.join(''));

        const resultadoFinal = arregloAgrupado.join('');
        console.log("------> FINAL FINAL FINAL FIANAAAAAAAAAAAL")
        console.log(resultadoFinal);

        console.log(`  Mensaje final -> ${resultadoFinal}`);
        console.log('\n-------------------------------------------------------------------\n');
        return resultadoFinal;
    }

    // Mensajes de adiós
}

module.exports = {
    decodeHamming,
    toWordedHam
};