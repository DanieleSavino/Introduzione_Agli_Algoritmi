import sys, os
from random import randint

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.ListaLinkata import Node
from random import randint


def lista_ordinata_di_duplicati(P):
    A = []
    while P != None:
        A.append(P.key)
        P = P.next
    
    A.sort()
    Q = R = None

    for i in range(len(A)-1, 0, -1):
        if A[i] == A[i-1]:
            if Q == None:
                R = Node(A[i])
                Q = R

            elif A[i] != R.key:
                R.next = Node(A[i])
                R = R.next
        
    return Q
    
def test(n, length):
    for _ in range(n):
        A = [randint(0, length) for _ in range(length)]

        D = {}
        for n in A:
            D[n] = D.get(n, 0) + 1

        B = sorted(set(t[0] for t in list(D.items()) if t[1] > 1), reverse=True)
        res = Node.fromArray(B)

        input = Node.fromArray(A)
        out = lista_ordinata_di_duplicati(input)

        print(f'{input} =>  {res} == {out}')

        assert res == out

test(1000, 1000)
            