from random import randint

"""
Dato un array A di n interi, si scriva un algoritmo iterativo
MaxSequenzaElementiUguali che calcoli il numero di elementi
della più lunga porzione di A costituita interamente da elementi
consecutivi uguali tra loro.
Ad esempio, se A = [5, 7, 3, 3, 8, 9, 9, 9, 5, 3, 2, 2], allora la risposta è 3
in quanto la porzione [9, 9, 9] è la più lunga formata da elementi
consecutivi tutti uguali.
"""

def MaxSequenzaElementiUguali(A):
    # Inizializziamo la massima sequenza a 0
    maxCount = 0

    # Teniamo conto del conto dell'attuale elemento
    currCount = 1

    for i in range(1, len(A)):

        # Se l'elemento precedente è ripetuto aumenta il contatore
        if A[i] == A[i-1]:
            currCount += 1

        # Altrimenti controlla se ha superato la massima sequenza e resetta il contatore
        else:
            maxCount = max(maxCount, currCount)
            currCount = 1

    # Controlla l'ultima sequenza
    return max(maxCount, currCount)

def test(n, length):
    for _ in range(n):
        A = []
        maxCount = 0
        i = 0
        while i < length:
            r = randint(1, length // 10 + 1)

            if r > length - i: r = length - i

            A += [i] * r
            i += r

            maxCount = max(maxCount, r)

        result = MaxSequenzaElementiUguali(A)
        print(f'{A} -> {result} == {maxCount}')

        assert result == maxCount

test(1000, 1000)
