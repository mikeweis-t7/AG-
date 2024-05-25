# FITNESS 

"""

fitness o valor de aptitud.
el valor de aptitud es el que proporciona el AG es la
unica retroalimentacion que recibe el motor para guiarlo
hacia una solucion.

En este proyecto, el valor de aptitud es el nro total de letras
de la suposicion que coinciden con la letra en la posicion de la
contraseña

"""

import random as rd

# generar una suposicion
def generate_parent(length, geneSet):
    # length: longitud de la suposicion.
    # geneSet: conjunto de genes.
    
    genes = []

    while len(genes) < length:
        a = length - len(genes)   # cantidad de genes restantes.   
        b = len(geneSet)    # longitud del conjunto de genes.
        sampleSize = min(a, b)
        
        genes.extend(rd.sample(geneSet, sampleSize))
    return ''.join(genes)


# valor de aptitud : Calcula el valor de aptitud comparando la suposición con la cadena objetivo.
def get_fitness(guess, target):
    # guess: es la suposición o la cadena propuesta que se desea evaluar.
    # target: es la cadena objetivo
    
    fitness = 0  # Inicializamos la aptitud en 0

    n = len(target) # longitud de la cadena objetivo
    for i in range(n):  # Iteramos sobre cada indice de la cadena objetivo
        expected = target[i]  # Obtenemos el caracter esperado en la posición i, en la cadena target
        actual = guess[i]  # Obtenemos el carácter actual en la posición i, en la cadena suposicion

        if expected == actual:  # Comparamos los caracteres 
            fitness += 1  # Incrementamos la aptitud si hay una coincidencia
    return fitness  # Devolvemos el valor de aptitud

# Código simplificado (alternativa)
"""
def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess)
        if expected == actual)
"""




geneSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # conjunto de genes.
target = "HELLO" # contraseña a adivinar, objetivo

n = len(target)     # longitud de la cadena target
for i in range(1000):
    suposicion = generate_parent(n, geneSet)     # suposicion sobre la cadena objetivo dada por la funcion generar_suposicion
    fitness = get_fitness(suposicion, target)    # valor de aptitud
    print(f"Suposición: {suposicion}, Valor de aptitud: {fitness}")
















