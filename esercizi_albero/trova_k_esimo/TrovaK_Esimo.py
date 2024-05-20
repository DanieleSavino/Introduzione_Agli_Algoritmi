import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node

def trova_K_esimo(P, k):
    if P.left != None:
        trova_K_esimo(P.left, k)
    
    print(P.key)

    if P.right != None:
        trova_K_esimo(P.right, k - 1)

def test():
    P = Node.fromArray([50, 30, 70, 20, 40, 60, 80])
    #print(P)
    print(trova_K_esimo(P, 5))

test()