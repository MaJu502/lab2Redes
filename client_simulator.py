from word_to_binary import toBinary, toWord
from Hamming.EmisorHam import emisor_Hamming
import socket
import random
import json
import os
from CRC32.CRCAlgorithm import calculateCRC
import string

HOST = "127.0.0.1"   #IP DEL SERVIDOR 
PORT = 65123
n_loops = 50000 #Cantidad de iteraciones
n_length = 8 #Longitud de las cadenas
n_prob = 0.1

def generar_palabra(longitud):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(longitud))

def random_binary_string(n):
    return ''.join([str(random.randint(0, 1)) for _ in range(n)])

def ruidoGen(payload, prob):
    mod_payload = []
    for cadena in payload:
        mod_payload.append(''.join([aplicar_ruido(bit, prob) for bit in cadena]))
    return mod_payload

def aplicar_ruido(bit, probabilidad):
    if random.random() < probabilidad:
        return '1' if bit == '0' else '0'
    return bit


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Connected to {HOST}')

    print("     -- Bienvenido --\n En este programa podrás enviar un mensaje desde un emisor a un receptor usando\n los algoritmos ya sea de Hamming (detección y corrección) o CRC32 (detección).")
    
    while True:
        print("\n >> Seleccione una opción:")
        print("     1. Calcular con código de Hamming")
        print("     2. Calcular con CRC32")
        print("     3. Salir")

        choice = input("\n >> Opción: ")

        if choice == '1':
            #hamming_code = calculate_hamming(data)
            print(" >> Código de Hamming")
            hammingData = emisor_Hamming(binarydata)
            print(hammingData)
            data = {
                "type": 0, #0 es hamming, 1 es CRC
                "message": binarydata,
            }
            # print("original message", filedata)
            print("original message (binary)", data["message"])
            print("sent message", " ".join(element for pair in hammingData for element in pair[0]))
            data["message"] = hammingData                
            s.sendall(json.dumps(data).encode('utf-8'))
        elif choice == '2':
            data_con_ruido = 0
            print('calculando...')

            for i in range(n_loops):
                binarydata = [random_binary_string(n_length)]

                data = {
                    "type": 1, #1 es CRC
                    "message": binarydata,
                }
                crc_value = calculateCRC(data["message"])
                # print("ascii message",filedata)
                # print("sent message", crc_value)


                #CAPA DE RUIDO

                final_message = ruidoGen(crc_value,n_prob)

                #Si son iguales, no hubo cambio
                if final_message != crc_value:
                    # print('Hubo cambio')
                    data_con_ruido += 1

                data["message"] = final_message


                s.sendall(json.dumps(data).encode('utf-8'))
            print(f"Se envio {data_con_ruido} datos con ruido de {n_loops}")
        elif choice == '3':
            break
        else:
            print(" >> ERROR: Opción inválida. Por favor, seleccione una opción válida.")

        

    
