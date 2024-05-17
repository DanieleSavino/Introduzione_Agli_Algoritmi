import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node

"""
Dato un albero binario non vuoto a valori interi T ed un suo
nodo v, il costo del cammino radice-v è definito come la somma
dei valori dei nodi nel percorso che va dalla radice al nodo v
(estremi inclusi).
Vogliamo calcolare il costo del massimo cammino radicefoglia di T.
Ad esempio nell'albero binario in figura, la risposta è 18, infatti
nell'albero sono presenti quattro diversi cammini radice-foglia
di costo 3, 18, 11 e -70, rispettivamente.
Dato il puntatore r al nodo radice di un albero binario non
vuoto a valori interi T, progettare un algoritmo ricorsivo che,
in tempo Θ(n), risolva il problema.
L'albero è memorizzato tramite puntatori e record a tre campi:
il campo key contenente il valore ed i campi lef t e right con i
puntatori al figlio sinistro e al figlio destro, rispettivamente
(questi puntatori valgono None in mancanza del figlio).
"""

def MassimoCammino(R):
    # Se è vuoto restituisce 0
    if R == None:
        return 0

    # Conta a sinistra
    left = MassimoCammino(R.left)

    # Conta a destra
    right = MassimoCammino(R.right)

    # Propaga il sottopercorso più lungo + il nodo stesso
    return max(left, right) + R.key

def test(n, length):
    for _ in range(n):
        R = Node.randomTree(length, 0, 100)
        print(R)
        print(MassimoCammino(R))

test(1, 5)