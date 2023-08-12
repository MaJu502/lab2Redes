from word_to_binary import toBinary, toWord
from Hamming.EmisorHam import emisor_Hamming
import socket
import random
import json
import os
from CRC32.CRCAlgorithm import calculateCRC


HOST = "127.0.0.1"   #IP DEL SERVIDOR 
PORT = 65123


def ruidoGen(payload, prob):
    mod_payload = []
    for cadena in payload:
        mod_payload.append(''.join([aplicar_ruido(bit, prob) for bit in cadena]))
    return mod_payload

def aplicar_ruido(bit, probabilidad):
    if random.random() < probabilidad:
        return '1' if bit == '0' else '0'
    return bit

#Your Code Here - Aplicar algoritmo seleccionado

    # CAPA DE APLICACION ---------mostrar el mensaje--------------------------


    # -----------------------------------------------------

        #  CAPA DE ENLACE ---------verificar integridad/corregir--------------------------
        
        #  si type es 0
        #      decodificacion = hamming(data)
        #  si type es 1
        #      decodificacion = crc(data)

        # -----------------------------------------------------
        #   CAPA DE PRESENTACION ---------decodificar el mensaje (pasarlo a letras)--------------------------
        


        # -----------------------------------------------------


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Connected to {HOST}')

    print("     -- Bienvenido --\n En este programa podrás enviar un mensaje desde un emisor a un receptor usando\n los algoritmos ya sea de Hamming (detección y corrección) o CRC32 (detección).")
    
    while True:
        print("\n >> Seleccione una opción:")
        print("     1. Ingresar mensaje manualmente")
        print("     2. Usar archivo de texto")
        print("     3. Salir")

        choice = input("\n >> Opción: ")
        binarydata = None

        if choice == '1':
            filedata = input("\n >> Ingrese el mensaje: ")
            binarydata = toBinary(filedata)
        elif choice == '2':
            file_name = input("\n >> Ingrese el nombre del archivo txt donde se encuentra el mensaje: ") + ".txt"

            if not os.path.exists(file_name):
                print(" >> El archivo no existe.")
                continue

            with open(file_name, 'r') as file:
                filedata = file.read()

            binarydata = toBinary(filedata)
        elif choice == '3':
            break
        else:
            print(" >> ERROR: Opción inválida. Por favor, seleccione una opción válida.")
            continue

        with open("binaryMessage.txt", 'w') as archivo:
            archivo.write(' '.join(binarydata))
            archivo.write('\n')

        while True:
            print("\n >> Seleccione una opción:")
            print("     1. Calcular con código de Hamming")
            print("     2. Calcular con CRC32")
            print("     3. Regresar a menu de ingreso de mensaje")

            choice = input("\n >> Opción: ")
            

            if choice == '1':
                #hamming_code = calculate_hamming(data)
                data_con_ruido = 0
                print(" >> Código de Hamming")
                hammingData = emisor_Hamming(binarydata)
                data = {
                    "type": 0, #0 es hamming, 1 es CRC
                    "message": binarydata,
                    "original": filedata,
                }
                print(" >> sent message without noise -> ", " ".join(element for pair in hammingData for element in pair[0]))

                #CAPA DE RUIDO                
                mensajitos = [sublist for sublist, _ in hammingData for sublist in sublist]
                codersss = [[item for item in sublist] for _, sublist in hammingData]

                noiseHam = []
                for hh in hammingData:
                    tempi = ruidoGen(hh[0], 0.01)
                    noiseHam.append((tempi, hh[1]))
                
                mensajitofiufiu = [sublist for sublist, _ in noiseHam for sublist in sublist]
                print(" >> sent message with noise -> ", mensajitofiufiu)
                codesfiufiu = [[item for item in sublist] for _, sublist in noiseHam]

                #Si son iguales, no hubo cambio
                if mensajitofiufiu != mensajitos:
                    print('Hubo cambio')
                    data_con_ruido += 1

                data["message"] = noiseHam               
                s.sendall(json.dumps(data).encode('utf-8'))
            elif choice == '2':
                data_con_ruido = 0

                data = {
                    "type": 1, #0 es hamming, 1 es CRC
                    "message": binarydata,
                }
                crc_value = calculateCRC(data["message"])
                print("ascii message",filedata)
                print("sent message", crc_value)


                #CAPA DE RUIDO

                final_message = ruidoGen(crc_value,0.01)

                #Si son iguales, no hubo cambio
                if final_message != crc_value:
                    print('Hubo cambio')
                    data_con_ruido += 1

                data["message"] = final_message


                s.sendall(json.dumps(data).encode('utf-8'))
            elif choice == '3':
                break
            else:
                print(" >> ERROR: Opción inválida. Por favor, seleccione una opción válida.")

    
