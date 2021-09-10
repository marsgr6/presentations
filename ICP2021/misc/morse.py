"""
Nombres:
Apellidos:
"""


# Diccionario espanol a morse
e2m = {'A': '.-',     'B': '-...',   'C': '-.-.',
       'D': '-..',    'E': '.',      'F': '..-.',
       'G': '--.',    'H': '....',   'I': '..',
       'J': '.---',   'K': '-.-',    'L': '.-..',
       'M': '--',     'N': '-.',     'O': '---',
       'P': '.--.',   'Q': '--.-',   'R': '.-.',
       'S': '...',    'T': '-',      'U': '..-',
       'V': '...-',   'W': '.--',    'X': '-..-',
       'Y': '-.--',   'Z': '--..',
       '0': '-----',  '1': '.----',  '2': '..---',
       '3': '...--',  '4': '....-',  '5': '.....',
       '6': '-....',  '7': '--...',  '8': '---..',
       '9': '----.'
       }


# Diccionario morse a espanol
m2e = {e2m[k]: k for k in e2m.keys()}


def eng2morse(mensaje):
    """
    Entrada: 'Hola Mundo'
    Salida: '.... --- .-.. .- / -- ..- -. -.. --- '
    Convierte un mensaje de esp a morse
    convierta el mensaje a mayusculas (use string.upper())
    Cree una cadena (string) vacia
    Recorra el mensaje letra y haga crecer la cadena anterior
    con el valor correspondiente a la letra (clave) en el
    diccionario, si la clave no existe devuleva '/', use get
    Concatene un espacio en blanco al final de cada ciclo
    Devuleva la cadena generada
    Nota: el caracter / representa en morse el espacio en blanco
    Valor: 30%
    """
    pass


def morse2eng(mensaje):
    """
    Entrada: '.... --- .-.. .- / -- ..- -. -.. --- '
    Salida: 'Hola Mundo'
    Haga un split de la cadena de entrada usando '/'
    para obtener las palabras
    Pase cada palabra a la funcion mor2engP()
    como una lista separada por espacios (split)
    (cada elemento sera una de las letras)
    La funcion mor2engP() devuleve la concatenacion
    de dichas letras como una palabra en espanol
    usando cada letra/clave del diccionario m2e y concatenando la salida

    Concatene la salida de mor2engP() para construir el mensaje completo
    Use cada palabra el mensaje usandola
    Salida: 'Hola Mundo'
    Valor: 30%
    """
    pass


def mor2engP(letras):
    """
    Entrada: ['....', '---', '.-..', '.-']
    Salida: '
    HOLA'
    Recibe cada palabra como una lista 
    (cada elemento es una de las letras)
    La funcion mor2engP() devuleve la concatenacion
    de dichas letras como una palabra en espanol
    usando cada letra/clave del diccionario m2e y concatenando la salida
    Valor: 20%
    """
    pass


def main(args):
    """
    Uso: python morseTranslator.py transFromTo text
    transFromTo: es2mor, mor2es
    text: texto a traducir
    Ejemplo: python morseTranslator.py es2mor 'Hola Mundo'
    Ejemplo: python morseTranslator.py mor2es '.... --- .-.. .- / -- ..- -. -.. --- '
    Valor: 20%
    """
    if len(args) != 2:
        print(main.__doc__)
    else:
        if args[0] == 'es2mor':
            print("Mensaje original")
            print("Mensaje traducido: ")
        elif args[0] == 'mor2es':
            print("Mensaje original")
            print("Mensaje traducido: ")
        else:
            print("Opcion traducir no valida")
            print(main.__doc__)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
