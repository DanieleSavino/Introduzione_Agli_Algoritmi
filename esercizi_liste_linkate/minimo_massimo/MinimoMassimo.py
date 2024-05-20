import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.ListaLinkata import Node
from random import randint

"""
Abbiamo una lista a puntatori contenente nodi con campo chiave contenente interi e vogliamo
sapere il valore massimo ed il valore minimo delle chiavi dei
nodi della lista.
Ad esempio per la lista a puntatori in figura la risposta è la
coppia di interi 9 e -4.
Dato il puntatore p al nodo testa della lista di n ≥ 1 nodi,
progettare un algoritmo ricorsivo che, in tempo Θ(n), risolva il
problema.
3
Ciascun nodo della lista ha due campi: il campo key contenente
il valore chiave ed il campo next al nodo seguente (next è pari
a None per l'ultimo nodo della lista).
Dell'algoritmo proposto:
"""

def MinimoMassimo(P):
    if P == None:
        return None, None

    if P.next == None:
        return P.key, P.key

    minimo, massimo = MinimoMassimo(P.next)

    return min(minimo, P.key), max(massimo, P.key)

def test(n, length):
    for _ in range(n):
        A = [randint(-length, length) for _ in range(length)]
        P = Node.fromArray(A)

        minimo, massimo = MinimoMassimo(P)
        print(f'{P} {minimo}, {massimo}')
        assert minimo == min(A) and massimo == max(A)

test(1000, 994)