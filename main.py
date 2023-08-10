import os
from word_to_binary import toBinary, toWord
from Hamming.EmisorHam import *

def main():
    print("     -- Bienvenido --\n En este programa podrás enviar un mensaje desde un emisor a un receptor usando\n los algoritmos ya sea de Hamming (detección y corrección) o CRC32 (detección).")
    
    while True:
        print("\n >> Seleccione una opción:")
        print("     1. Ingresar mensaje manualmente")
        print("     2. Usar archivo de texto")
        print("     3. Salir")

        choice = input("\n >> Opción: ")

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
            print(" >> binary data inicial generada --> ", binarydata)
            print("\n")
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
                print(" >> Código de Hamming")
                hammingData = emisor_Hamming(binarydata)
                print(hammingData)
                data = {
                    "type": 0, #0 es hamming, 1 es CRC
                    "message": binarydata,
                }
                print("original message", filedata)
                print("original message (binary)", data["message"])
                print("sent message", " ".join(element for pair in hammingData for element in pair[0]))

            elif choice == '2':
                #crc_value = calculate_crc32(data)
                print(" >> Valor CRC32")
            elif choice == '3':
                break
            else:
                print(" >> ERROR: Opción inválida. Por favor, seleccione una opción válida.")

main()
