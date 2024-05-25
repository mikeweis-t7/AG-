# GENERAR UNA SUPOSICION - GENES
"""

El codigo esta diseñado para generar suposiciones aleatorias que tienen la misma longitud que una cadena objetivo.

"""

import random as rd

geneSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # conjunto de genes.
target = "HELLO" # contraseña a adivinar, objetivo

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



n = len(target) # longitud de la contraseña objetivo.
for i in range(1000000):
    suposicion = generate_parent(n, geneSet)
    print(suposicion)

