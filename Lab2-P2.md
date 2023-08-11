## Instrucciones para ejecutar Simluacion
Para este procedimiento se puede definir las siguientes variables dentro del archivo client_simulator.py para controlar los parametros de la simulacion.

n_loops = 50000 #Cantidad de iteraciones
n_length = 8 #Longitud de las cadenas
n_prob = 0.1 #probabilidad de error

- Paso 1: ejecutar en terminal node server_receptor.js (servidor/receptor)
- Paso 2: ejecutar en terminal python .\client_simulator.py (cliente/emisor)
- Paso 3: seguir instrucciones en terminal

NOTA: Para ver el mensaje en el receptor, debe terminar el proceso del emisor

Output: 
Lado del cliente (emisor): se mostrará la cantidad de mensajes con error enviados 
Lado del servidor: se mostrará la cantidad de mensajes con error detectados (verificar NOTA)

## Instrucciones para ejecutar envio de mensajes individuales
En este proceso, se permite el ingreso de un mensaje 

- Paso 1: ejecutar en terminal node server_receptor.js (servidor/receptor)
- Paso 2: ejecutar en terminal python .\client_simulator.py (cliente/emisor)
- Paso 3: seguir instrucciones en terminal para enviar mensaje desde el emisor

NOTA: Para ver el mensaje en el receptor, debe terminar el proceso del emisor

Output: 
Lado del cliente (emisor): 
    - se preguntará el formato en el que se quiere enviar un mensaje
    - se preguntará el algoritmo que será utilizado para enviar el mensaje

Lado del servidor: 
    - se mostrará en pantalla el mensaje recibido 
    - se mostrará en pantalla la cantidad de errores detectados (verificar NOTA)