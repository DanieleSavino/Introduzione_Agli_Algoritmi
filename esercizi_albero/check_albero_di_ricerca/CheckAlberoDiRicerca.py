import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node

""" 
    Progettare un algoritmo che, dato il puntatore alla radice
    di un albero binario T avente per chiavi degli interi, verifica se l'albero `e un albero
    binario di ricerca.
    Ad esempio, l'algoritmo per l'albero sulla sinistra deve restituire T rue mentre per
    l'albero sulla destra deve restituire F alse (infatti nel sottoalbero di sinistra del
    nodo con chiave 3 `e presente un nodo con chiave 4)
    Il costo computazionale dell'algoritmo proposto deve essere Θ(n) dove n `e il
    numero di nodi dell'albero.
    Dell'algoritmo proposto
"""

def check_albero_di_ricerca(P, n_min=None, n_max=None):
    # Se l'albero è vuoto soddisfa la definizione di albero di ricerca
    if P == None: return True

    # Se n_min è None il nodo non fa parte di nessun sottoalbero destro, percui non ha nessun vincolo sul minimo
    # Se invece n_min è un numero maggiore di P.key l'albero non è di ricerca
    if n_min != None and P.key < n_min:
        return False
    
    # Se n_max è None il nodo non fa parte di nessun sottoalbero sinistro, percui non ha nessun vincolo sul massimo
    # Se invece n_max è un numero minore di P.key l'albero non è di ricerca
    if n_max != None and P.key > n_max:
        return False
    
    # Richiamiamo a sinistra propagando n_min e aggiornando il max a P.key
    left = check_albero_di_ricerca(P.left, n_min, P.key)
    if not left:
        return False
    
    # Richiamiamo a destra propagando n_max e aggiornando il min a P.key
    right = check_albero_di_ricerca(P.right, P.key, n_max)
    if not right:
        return False
    
    # Se passiamo tutti i controlli l'albero è di ricerca
    return True

def test():
    P = Node.fromArray([10, 7, 15, 3, 9, 12, 20, None, None, None, None, None, 14])
    Q = Node.fromArray([3, 2, 10, 1, 4, 6, 20, None, None, None, None, None, 8])
    print(f'{P} ==> {check_albero_di_ricerca(P)}\n\n')
    print(f'{Q} ==> {check_albero_di_ricerca(Q)}')

test()