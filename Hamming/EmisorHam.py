# Universidad del Valle de Guatemala
# Marco Jurado 
# Cristian Aguirre
# redes



def emisor_Hamming(mensaje):
    # leer el txt donde esta el mensaje
    try:
        mensaje = "Hamming\\" + mensaje + ".txt" # para finalidades de ejecución
        with open(mensaje, 'r') as archivo:
            a = archivo.readline().strip()
        a = a.replace(' ', '')

        # Calcular la cantidad de ceros necesarios para completar el último conjunto
        ceros_faltantes = (4 - len(a) % 4) % 4
        a += '0' * ceros_faltantes

        # Separar el mensaje en conjuntos de 4 elementos
        conjuntos_de_4 = [a[i:i+4] for i in range(0, len(a), 4)]

        retorno = []
        for y in conjuntos_de_4:
            retorno.append(procesoHamming(y))

        mensajes = []
        codes = retorno[0][1]
        for u in retorno:
            mensajes.append(u[0])
        
        retorno_str = [str(num) for num in mensajes]
        codes = [str(x) for x in codes]
        codes = '-'.join(codes)
        codes = codes.replace('[', '')
        codes = codes.replace(']', '')
        codes = codes.replace(', ', '')
        codes = codes.replace('-', ' ')
        


        # Abrir el archivo en modo escritura ('w') y escribir los números de retorno
        with open("Hamming//codedMessageHamming.txt", 'w') as archivo:
            archivo.write(' '.join(retorno_str))
            archivo.write('\n')
            archivo.write(codes)
        
        print(" -> Mensaje codificado en codedMessageHamming.txt ")

    except FileNotFoundError:
        print(f"Error: El archivo '{mensaje}' no fue encontrado.")
        return None

def procesoHamming(a):
    # paso 1 contar bits
    bits = len(a)
    
    # paso 2 buscar que satisface la ecuacion 
    factor = 0
    while 2 ** factor < bits + factor + 1:
        factor += 1

    temp_total = 2 ** factor

    # paso 3 calcular bits para codificar con el factor encontrado
    casillas_mod = []
    for i in range(factor):
        casillas_mod.append((2 ** i)-1)
    
    retorno = []
    casillas_x = []
    for t in range(bits + factor):
        if t in casillas_mod:
            retorno.append('x')
            casillas_x.append(t)
        else: 
            retorno.append('y')

    for i in a:
        for j,h in enumerate(retorno):
            if retorno[j] == "y":
                retorno[j] = i
                break

    # escribir tabla
    nueva_tabla = []
    for i in casillas_mod:
        listita = []
        unos = []
        for j in range(temp_total):
            if (int((j/(i+ 1)) % 2)) == 0:
                listita.append(0)
            else:
                listita.append(1)

        nueva_tabla.append((listita,unos)) 

    para_obtener_paridad = []
    for i in nueva_tabla:
        a_obtener = []
        for h,j in enumerate(i[0]):
            if j == 1:
                a_obtener.append(h-1)  
        para_obtener_paridad.append(a_obtener)

    for i in para_obtener_paridad:
        contz = 0
        contu = 0
        for j,h in enumerate(retorno):
            if j in i:
                if h == "1":
                    contu += 1
                if h == "0":
                    contz += 1

        for y in i:
            if retorno[y] == "x":
                if contz < contu:
                    retorno[y] = 0
                if contu < contz:
                  retorno[y] = 1
                
    retorno = retorno[::-1]

    # Juntar los elementos en una cadena
    hammingCode = ''.join(str(item) for item in retorno)
    return hammingCode,para_obtener_paridad

emisor_Hamming("mensajeHam_ingresado")