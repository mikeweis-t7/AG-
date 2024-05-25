# MAIN - 1

import random as rd
import datetime

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


# mutacion
def mutate(parent, geneSet):
    # parent: cadena suposicion
    # geneSet: conjunto de genes
    
    index = rd.randrange(0, len(parent))  # Extraemos un indice al azar de la cadena 'parent'.
    childGenes = list(parent)  # Convertimos 'parent' en una lista de caracteres.
    newGene, alternate = rd.sample(geneSet, 2)  # Seleccionamos dos elementos al azar de 'geneSet'.
    # Si 'newGene' es igual al caracter en 'index', usamos 'alternate'. De lo contrario, usamos 'newGene'.
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)  # Convertimos la lista de nuevo a una cadena y la retornamos.

# display:
def display(guess, target):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess, target)
    print("Monitoreo  {}\t{}\t{}".format(guess, fitness, timeDiff))



# Definición del conjunto de genes y la cadena objetivo
geneSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Conjunto de genes.
target = "HELLO"  # Contraseña a adivinar, objetivo.

# Longitud de la cadena target
n = len(target)

# Inicialización inicial
rd.seed()
startTime = datetime.datetime.now()
parent = generate_parent(n, geneSet)
fitness = get_fitness(parent, target)

# Mostrar resultados iniciales
print("Suposición inicial:", parent)
print("Valor de aptitud de la suposición inicial:", fitness)
display(parent, target)  # Mostrar monitoreo inicial





