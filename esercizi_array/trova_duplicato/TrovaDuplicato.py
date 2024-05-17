from random import randint

""" 
In un array ordinato A di n interi compaiono tutti gli interi da
0 ad n-2. Esiste dunque nell'array un unico elemento duplicato.
Si progetti un algoritmo ITERATIVO che, dato A, in tempo
Θ(log n) restituisca l'elemento duplicato.
Ad esempio, per A = [ 0, 1, 2, 3, 4, 4, 5, 6, 7 ] l'algoritmo deve restituire 4.
"""

def TrovaDuplicato(A):
    # Inizializza i e j
    i = 0
    j = len(A) - 1

    while(i < j):
        # Trova la metà
        m = (i+j)//2
        
        # Se il valore a metà è minore del suo indice abbiamo passato il valre duplicato.
        # Percui cerchiamo nel sottoarray precedente
        if A[m] < m:
            j = m 

        # Altrimenti cerchiamo nel sottoarray successivo
        else:
            i = m + 1
    
    # Se i == j abbiamo trovato l'elemento duplicato
    return A[i]

def test(n, length):
    for _ in range(n):
        A = []

        i = 0
        r = randint(0, length-2)

        for _ in range(length-1):
            A.append(i)
            if i == r: A.append(i)
            i += 1

        dup = TrovaDuplicato(A)
        print(f'{A} -> {dup} == {r}')

        assert dup == r

    
test(1000, 1000)