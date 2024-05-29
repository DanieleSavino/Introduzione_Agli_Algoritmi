import sys, os
from random import randint

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.ListaLinkata import Node
from random import randint

""" 
Si consideri una lista a puntatori circolare L data tramite un puntatore p ad un
suo elemento. In L ogni nodo ha 2 campi: il campo key contenente un intero ed
il campo next con il puntatore al nodo seguente.
Sappiamo che gli interi dei vari nodi sono tutti distinti e bisogna trovare il valore
minimo tra questi. Ad esempio per la lista circolare di seguito il valore cercato `e
3:
3
Progettare un algoritmo iterativo che, dato il puntatore p ad un nodo della lista
circolare, restituisce il valore cercato in tempo Θ(n) dove n `e il numero di nodi
della lista.
"""

def min_lista_circolare(P):
    if P == None:
        return None
    
    x = m = P.key
    P = P.next

    while P.key != x:
        m = min(m, P.key)
        P = P.next

    return m
    
def test(n, length):
    for _ in range(n):
        A = list(set(randint(-length, length) for _ in range(length)))
        P = Node.fromArray(A)
        res = min(A)

        Q = P
        while Q.next != None:
            Q = Q.next

        Q.next = P
        out = min_lista_circolare(P)
        print(f'{A} => {res} == {out}')
        assert res == out

test(1000, 1000)

