# lab2Redes
## Instrucciones para ejecutar Hamming

Este es un programa que implementa el algoritmo de Hamming para codificar y decodificar mensajes. Siga los pasos a continuación para ejecutarlo correctamente:

1. Escribir mensaje a codificar:
   - Abra el archivo de texto con el nombre "mensajeHam_ingresado.txt".
   - Escriba el mensaje que desea codificar en una sola línea dentro del archivo.
   - Guarde los cambios y cierre el archivo.

2. Codificar el mensaje:
   - Ejecute el programa de Python que implementa el algoritmo Hamming.
   - Puede hacerlo presionando la tecla F5 en su entorno de desarrollo o mediante el siguiente comando en la línea de comandos:
     ```
     python EmisorHam.py
     ```
   - El resultado de la codificación se almacenará en el archivo de texto "codedMessageHamming.txt".

3. Decodificar el mensaje:
   - Nota: Si desea cambiar el codigo para manualmente ingresar errores debe de hacerlo en el archivo de texto "codedMessageHamming.txt".
   - Ejecute el programa de Java que se encarga de descodificar el mensaje previamente codificado.
   - El programa leerá el contenido del archivo "codedMessageHamming.txt" y realizará la decodificación.
   - Dependiendo del resultado, se le notificará si el código contiene errores y, si es así, se corregirán automáticamente. En caso contrario, se le informará que el código está correcto.

¡Listo! Ahora debería tener el mensaje original decodificado y listo para su lectura.

Recuerde que tanto el programa de Python como el de Java deben estar en el mismo directorio que los archivos de texto mencionados para que el proceso de codificación y decodificación funcione correctamente.


## Instrucciones para ejecutar CRC32


1. Generar el mensaje: 
   ----------------- Comando -----------------
   python .\CRC32\emisor.py >Trama a ingresar<
   -------------------------------------------
   Este programa recibe como argumento la trama que se quiere enviar y aplica el algoritmo CRC32 para calcular los bits de paridad. Este programa utiliza el polinomio 