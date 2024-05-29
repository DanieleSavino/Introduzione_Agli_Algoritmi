import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node
from random import randint

""" 
    Sia dato un albero binario T, in cui ogni nodo p ha
    tre campi: il campo valore p.val, il campo col puntatore al figlio sinistro p.sx e il
    campo col puntatore al figlio destro p.dx, in mancanza di figlio il puntatore vale
    None.
    Progettare un algoritmo ricorsivo che, dato il puntatore p alla radice dell'albero
    binario T, restituisca 1 se tutti i nodi dell'albero hanno lo stesso valore, 0 altrimenti.
    Il costo computazionale dell'algoritmo deve essere O(n), dove n `e il numero di nodi
    dell'albero.
"""

def nodi_uguali(T):
    if T == None:
        return 1
    
    if nodi_uguali(T.left) == 0:
        return 0
    
    if nodi_uguali(T.right) == 0:
        return 0

    if (T.left == None or T.key == T.left.key) and (T.right == None or T.key == T.right.key):
        return 1
    
    return 0

def test(n, length):
    for _ in range(n):
        A = [randint(-length//10, length//10) for _ in range(length)]

        compare = A[0]
        res = 1
        for n in A:
            if n != compare:
                res = 0
                break

        T = Node.fromArray(A)
        out = nodi_uguali(T)

        print(f'{T}\n\n{out} == {res}\n')
        assert res == out

test(1000, 5)