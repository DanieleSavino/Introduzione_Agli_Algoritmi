import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node

""" 
Dato il puntatore r al nodo radice di
un albero binario non vuoto, progettare un algoritmo ricorsivo
che in tempo Θ(n) calcoli il numero di nodi che hanno esattamente 2 figli e chiave pari.
Ad esempio, per l'albero in figura, l'algoritmo deve restituire
2, per la presenza dei nodi con chiavi 2 e 0.
L'albero è memorizzato tramite puntatori e record di tre campi: il campo key contenente il valore ed i campi lef t e right con
i puntatori al figlio sinistro e al figlio destro, rispettivamente
(questi puntatori valgono None in mancanza del figlio). 
"""

def conta_nodi(R):
    # Se è vuoto restituisce 0
    if R == None:
        return 0
    
    # Inizializza left e right
    left = right = 0

    # Conta a sinistra
    if R.left != None:
        left = conta_nodi(R.left)

    # Conta a destra
    if R.right != None:
        right = conta_nodi(R.right)

    # Se soddisfa la condizione restituisce 1 + la somma dei sottonodi validi
    if R.left != None and R.right != None and R.key % 2 == 0:
        return left + right + 1
    
    # Altrimenti propaga la somma dei sottonodi validi
    return left + right

def test(n, length):
    for _ in range(n):
        R = Node.randomTree(length, -100, 100)
        print(R)
        print(conta_nodi(R))

test(1, 10)