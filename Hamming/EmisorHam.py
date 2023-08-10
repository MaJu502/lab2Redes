# Universidad del Valle de Guatemala
# Marco Jurado 
# Cristian Aguirre
# redes



def emisor_Hamming(binaryinfo):
    """# leer el txt donde esta el mensaje
    mensaje = "Hamming\\" + mensaje + ".txt" # para finalidades de ejecución
    with open(mensaje, 'r') as archivo:
        a = archivo.readline().strip()
    a = a.replace(' ', '')"""
    data = []
    for i in binaryinfo:
        """ 
        Por cada caracter del mensaje primero se completan 
        los cero que hagan faltapara hamming
        """
        ceros_faltantes = (4 - len(i) % 4) % 4
        i += '0' * ceros_faltantes
        conjuntos_de_4 = [i[x:x+4] for x in range(0, len(i), 4)]

        """
        Ahora que ya estan los ceros y los conjuntos de 4 bits
        podemos codificar dicha cadena con hamming.
        """
        retorno = []
        for y in conjuntos_de_4:
            retorno.append(procesoHamming(y))

        mensajes = []
        codes = retorno[0][1]
        for u in retorno:
            mensajes.append(u[0])
        
        retorno_str = [str(num) for num in mensajes] # cadena codificada
        codes = [str(x) for x in codes]
        codes = [''.join(char for char in code if char.isdigit()) for code in codes] # bits de paridad obtenidos

        data.append((retorno_str, codes))
    
    return data

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