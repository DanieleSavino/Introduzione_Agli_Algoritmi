from random import randint

"""  
    Sia dato un array A contenente n interi distinti e ordinati in
    modo crescente.
    Progettare un algoritmo che, in tempo O(log n), individui la posizione più a sinistra nell'array per cui si ha A[i] 6= i,l'algoritmo
    restituisce -1 se una tale posizione non esiste.
"""

def primo_elemento_diverso_da_i(A):
    # Se il primo elemento è diverso da 0 lo abbiamo trovato
    # Altrimenti la lista sarà ordinata di interi positivi
    if A[0] != 0: return 0

    # Inizializziamo gli indici
    i, j = 0, len(A)-1

    # Ricerca binaria
    while i < j:
        # Calcola il centro
        m = (i+j)//2
        
        # Se l'elemento centrale è al posto i l'elemento che cerchiamo sarà a destra
        # Poiche abbiamo verificato all'inizio che l'array parte da 0, quindi, A[0:m+1] = [0, 1, ..., m-1, m]
        if A[m] == m:
            i = m + 1
        
        # Altrimenti l'elemento è a sinistra m compreso
        else:
            j = m

    # Alla fine rimarrà un indice i == j che controliamo
    if A[i] != i: return i

    # Se non è questo ritorniamo -1
    return -1 

def test(n, length):
    for _ in range(n):
        A = sorted(set(randint(-1, length*2) for _ in range(length)))

        res = -1
        for i, n in enumerate(A):
            if i != n:
                res = i
                break

        out = primo_elemento_diverso_da_i(A)
        print(f'{A} =>  {res} == {out}')
        assert res == out

test(1000, 1000)