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
    except FileNotFoundError:
        print(f"Error: El archivo '{mensaje}' no fue encontrado.")
        return None
    
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
    
    # escribir tabla
    nueva_tabla = []
    for i in casillas_mod:
        listita = []
        for j in range(temp_total):
            if (int((j/(i+ 1)) % 2)) == 0:
                listita.append(0)
            else:
                listita.append(1)

        nueva_tabla.append(listita) 

    
    pass    

emisor_Hamming("mensajeHam")