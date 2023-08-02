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

    # paso 3 calcular bits para codificar con el factor encontrado
    for i in range(factor):
        temp = 2 ** i
    pass    

emisor_Hamming("mensajeHam")