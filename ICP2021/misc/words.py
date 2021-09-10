"""
Nombres:
Apellidos:
"""


import string as s


def readFile(archivo):
    """
    Lee un archivo de texto y devuelve una
    lista donde cada elemento es una palabra
    del texto
    Entrada: archivo.txt
      Hola mundo
      en un archivo
    Salida: ['hola','mundo','en','un','archivo']
    Nota: devuelva las palabras en minusculas
    Valor: 10%
    """
    pass


def countFreq(words):
    """
    Recibe una lista conteniendo palabras
    Construya un diccionario utilizando
    como claves cada palabra unica (use set)
    Los valores del diccionario seran las frecuencias
    correspondientes a cada clave (palabra)
    Devuelva el diccionario
    Ejemplo de entrada ['en','este','mes','en', 'este', 'dia']
    Salida {'en': 2, 'este': 2, 'mes': 1, 'dia': 1}
    Valor: 20%
    """
    pass


def makedictA():
    """
    Construya un diccionario a partir de las letras
    minusculas del alfabeto, use la letra como clave
    y a cada valor asigne 0
    Tip: use string.lower para obtener las letras
    Salida:
    {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 
    'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 
    'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 
    'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
    Valor: 10%
    """
    pass


def countFreqA(dictA, words):
    """
    Cuenta las frecuencias de la letra
    con que empieza cada palabra en la 
    lista words
    Entradas: 
    dictA:
    {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 
    'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 
    'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 
    'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
    words: lista generada al leer el archivo
    Salida:
    {'a': 35, 'c': 16, 'b': 11, 'e': 11, 'd': 10, 'g': 7, 'f': 9, 
    'i': 11, 'h': 29, 'k': 1, 'j': 2, 'm': 13, 'l': 4, 'o': 22, 'n': 3, 
    'q': 0, 'p': 9, 's': 11, 'r': 4, 'u': 1, 't': 24, 'w': 16, 'v': 4, 
    'y': 2, 'x': 1, 'z': 0}
    Valor: 20%
    """
    pass


def printFreq(freq):
    """
    Recibe un diccionario e imprime 2 columnas
    claves frecuencias, en orden alfabetico
    Ejemplo:
    Entrada {'en': 2, 'este': 2, 'mes': 1, 'dia': 1}
    Impresion:
    dia 1
    en 2
    este 2
    mes 1
    Valor: 10%
    """
    pass


def main(args):
    """
    Uso: python wordsFreq.py archivo
    archivo: nombre del archivo
    Ejemplo: python wordsFreq.py palabras.txt
    Valor: 30%
    """
    if len(args) != 1:
        print main.__doc__
    else:
        print "Total palabras: "
        print "Frecuencias por letras"
        print "Frecuencias de palabras"


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
