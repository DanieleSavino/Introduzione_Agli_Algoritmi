import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.AlberoBinario import Node

def figli_uguali(R):
    if R == None:
        return 0
    
    left = figli_uguali(R.left)
    right = figli_uguali(R.right)

    x = 0
    if R.left and R.right and R.right.key == R.left.key:
        x = 1

    return left + right + x

def test():
    R = Node.fromArray([6, 2, 3, 4, 6, 4, 7, 13, 8, None, 9, 12, 10])
    R2 = Node.fromArray([6, 3, 3, 6, 5, 1, 1, 2, 2, None, 9, 12, 10])

    print(figli_uguali(R))
    print(figli_uguali(R2))

test()