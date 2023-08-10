# Marco Jurado 
# Cristian Aguirre

"""
param: recibe 'x' mensaje completo ingresado por usuario para ser
       codificado y convertido a binario para ser enviado. 
"""
def toBinary(x):
    retorno = []
    for i in x:
        retorno.append(format(ord(i), '08b'))
    return retorno

"""
param: recibe 'x' mensaje completo binario para ser descodificado
       a palabra. 
"""
def toWord(x):
    binary_list = x # arreglo 
    char_list = []

    for binary_code in binary_list:
        decimal_value = int(binary_code, 2)  # Convierte el código binario a decimal
        char_list.append(chr(decimal_value))  # Convierte el valor decimal a un caracter y agrega a la lista

    return ''.join(char_list)  # Une la lista de caracteres en una cadena