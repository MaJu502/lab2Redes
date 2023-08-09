import socket

import json

data = {
    "type": 0, #0 es hamming, 1 es CRC
    "01000": "2462",
}

HOST = "127.0.0.1"   #IP DEL SERVIDOR 
PORT = 65123

#Your Code Here - Aplicar algoritmo seleccionado


# mensaje_a_enviar = [{cadena binaria + bit de paridad} , {cadena binaria + bit de paridad}, ...]
#--------------

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(json.dumps(data).encode('utf-8'))
