import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node
""" 
Un nodo di un albero a valori interi si dice nodo valido
se la somma dei valori dei suoi antenati `e uguale al valore del nodo. Ad esempio
nell'albero binario in figura, risultano validi 3 nodi (quello con valore 0, quello con
valore 9 e quello con valore -35 ).
Dato il puntatore r al nodo radice di un albero binario non vuoto, progettare un
algoritmo ricorsivo che in tempo Θ(n) calcoli il numero di nodi validi dell'albero.
L'albero `e memorizzato tramite puntatori e record a tre campi: il campo key
contenente il valore ed i campi lef t e right con i puntatori al figlio sinistro e
al figlio destro, rispettivamente (questi puntatori valgono None in mancanza del
figlio).
"""

def conta_nodi_validi(P, c=0):
    # Se usciamo dall'albero ritorniamo 0
    if P == None: return 0

    # Incrementiamo il contatore per le prossime chiamate
    next = c + P.key

    # richiamiamo a destra e sinistra
    left = conta_nodi_validi(P.left, next)
    right = conta_nodi_validi(P.right, next)

    # Se il nodo è valido incrementa di 1
    if P.key == c:
        return 1 + left + right
    
    # Altrimenti propaga il risultato
    return left + right

def test(n, length):
    P = Node.fromArray([0, 2, 5, 1, 7, 6, -40, None, None, 9, None, None, None, -35, None])
    print(P)
    print(f'{conta_nodi_validi(P)}\n')

    for _ in range(n):
        P = Node.randomTree(length, -length//3, length//3)
        print(P)
        print(f'\n{conta_nodi_validi(P)}\n')

test(1, 10)