import sys, os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(parent_dir)

from strutture_dati.ListaLinkata import Node
from random import randint

""" 
Sia L una lista concatenata semplicemente puntata
data tramite il puntatore p alla sua testa e contenenti chiavi intere positive. Ogni
record `e composto da due campi: il campo key che contiene il valore del nodo
ed il campo next che contiene il puntatore al nodo successivo della lista se questo
esiste, il valore None altrimenti. Si progetti un algoritmo ricorsivo con costo
computazionale O(n) che restituisca un puntatore al primo elemento della lista
la cui chiave sia esattamente uguale alla somma delle chiavi di tutti gli elementi
precedenti; se un tale elemento non esiste, verr`a ritornato None.
Ad esempio, per la lista p → 1 → 2 → 3 → 6 verr`a restituito un puntatore al
record contenente l'informazione 3; si noti che anche il record contenente l'informazione 6 soddisfa la richiesta di avere la chiave pari alla somma dei precedenti,
ma il record contenente 3 lo precede.
"""

def primo_nodo_somma(P, c=0):
    # Se siamo usciti dalla lista l'elemento non è presente
    if P == None: return None

    # Se la key è uguale al contatore abbiamo trovato l'elemento
    if P.key == c: return P

    # Altrimenti cerca più avanti
    return primo_nodo_somma(P.next, c + P.key)

def test(n, length):
    for _ in range(n):
        A = [randint(-length//3, length//3) for _ in range(length)]

        c = 0
        res = None
        for n in A:
            if n == c:
                res = n
                break
            c += n

        P = Node.fromArray(A)
        out = primo_nodo_somma(P)
        if out != None:
            out = out.key

        print(f'{P}  =>  {res} == {out}')
        assert res == out
    
test(100, 100)