import sys

def gen_txt(contenido, filename):
    try:
        with open(f'./CRC32/{filename}.txt', 'w') as archivo:
            archivo.write(contenido)
    except Exception as e:
        return 

def DivideXOR(trama:list, polinomio:list):
    '''Esta función toma dos cadenas binarias como parámetros de entrada y calcula 
    su resultado XOR (O exclusivo). La operación XOR se realiza en los bits correspondientes 
    de las dos cadenas binarias, resultando en una nueva cadena binaria que representa la 
    operación lógica XOR entre las dos entradas.'''
    result = []
    for i, bit in enumerate(polinomio):
        result.append(str(int(trama[i]) ^ int(bit)))
    return result


def CRC32(input:str, pol:str):
    #Definicion de valores
    polinomio = list(pol)
    residuo = list('0'*(len(polinomio)-1))
    trama = list(input)

    #Agregar bits a la trama original. Ej 1010 -> 1010 + 000 = 1010000
    trama.extend(residuo)


    #Inicializamos con los primeros n(longitud del polinomio) bits de la trama original
    result = trama[:len(polinomio)]

    #Repetimos por cada bit extra de la trama
    for i in range(len(trama)-len(polinomio)+1):
        if result[0] == '1':
            result = DivideXOR(result, polinomio)
        else:
            result = DivideXOR(result, ['0' for _ in range(len(polinomio))])
        # eliminamos el primer bit del resultado.
        result.pop(0)
        #Si todavia hay bits por baja en la trama original. 
        if i != (len(trama)-len(polinomio)+1) - 1:
            # bajamos el bit siguiente de la trama original.
            result.append(trama[(len(polinomio)+i)])

    return result[-(len(polinomio)-1):]


def calculateCRC(message):
    pol = '100000100110000010001110110110111'

    result_message = []

    for trama in message:
        #Calculamos los bits con el algoritmo
        bitparidad = "".join(CRC32(trama, pol))
        #A nuestra trama original agregamos los bits calculados
        unit_result = trama + bitparidad

        gen_txt(message, 'message')
        gen_txt(pol, 'polinomio')

        result_message.append(unit_result)

    return result_message
        

