import sys, os
from random import randint

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.ListaLinkata import Node
from random import randint

def MinimaSommaMinoreK(P, k):
    if k <= P.key:
        return 1
    return 1 + MinimaSommaMinoreK(P.next, k-P.key)

def test(n, length):
    for _ in range(n):
        A = [randint(0, length) for _ in range(length)]
        k = randint(0, sum(A))
        P = Node.fromArray(A)
        i = 0
        s = 0
        for n in A:
            if s >= k:
                break
            i += 1
            s += n

        res = MinimaSommaMinoreK(P, k)
        print(f'{P} k = {k} ==> {res} == {i}')
        assert res == i

test(100, 100)


