import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.ListaLinkata import Node
from random import randint

"""
Data una lista a puntatori P di nodi, progettare un algoritmo iterativo che restituisce una lista a puntatori Q di nodi contenente le chiavi pari
di P, in ordine crescente e senza ripetizioni
"""

def ChiaviPari(P):
    A = []
    if P == None:
        return None

    while P != None:
        if(P.key % 2 == 0):
            A.append(P.key)
        P = P.next

    A.sort(reverse=True)

    Q = Node(A.pop())
    R = Q

    while len(A) > 0:
        n = A.pop()
        if n != Q.key:
            Q.next = Node(n)
            Q = Q.next

    return R

def test(n, length):
    for _ in range(n):
        A = [randint(-length, length) for m in range(length)]
        P = Node.fromArray(A)
        A = list(dict.fromkeys(sorted([m for m in A if m % 2 == 0])))
        Q = Node.fromArray(A)
        R = ChiaviPari(P)
        print(f'{P} ==>  {Q} == {R}')

        while R != None and Q != None:
            assert R.key == Q.key
            R = R.next
            Q = Q.next

        if R != None or Q != None:
            assert False

test(1000, 1000)

