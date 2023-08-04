
polynomial = '1001'
polynomial = "100000100110000010001110110110111"


def gen_txt(contenido):
    try:
        with open('message.txt', 'w') as archivo:
            archivo.write(contenido)
    except Exception as e:
        return 

def XOR(b1, b2):
    result = '1' if b1 != b2 else '0'
    return result 

def CRC32(trama):
    #Trama + n 0s
    tempCode = trama + ('0'*(len(polynomial)-1))

    #Trama - bits de inicio
    new_t = tempCode[len(polynomial):]

    while True:
       
        result = ''
        # print(tempCode)
        # print(polynomial)
        # print('----------')

        for i, bit in enumerate(polynomial):
            result += XOR(bit, tempCode[i])
        
        # print(result,'\n')

        #Eliminamos los 0 antes del primer 1
        #Ej. 010 -> 10
        temp_result = result
        result = result.lstrip('0')

        if result == '' and ('1' not in new_t):
            print('resultado',result[-(len(polynomial)-1):])
            return '0'*(len(polynomial)-1)

        #Calculamos el desplazamientos de bits que hay que bajar de la trama original 
        temp = ''
        lenNew = len(polynomial) - len(result)

        if len(new_t) >= lenNew:
            #Por cada desplazamiento que hubo
            for i in range(lenNew):
                
                #Sacamos un bit de la trama original
                temp += new_t[0]
                #Eliminamos ese bit de la trama original 
                new_t = new_t[1:]
        else:
            return temp_result[-(len(polynomial)-1):]



        tempCode=result + temp

        




trama = '10001'
gen_txt(trama + CRC32(trama))