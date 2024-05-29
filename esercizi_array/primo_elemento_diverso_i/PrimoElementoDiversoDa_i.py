from random import randint

def primo_elemento_diverso_da_i(A):
    if A[0] < 0: return 0

    i, j = 0, len(A)-1

    while i < j:
        m = (i+j)//2
        
        if A[m] == m:
            i = m + 1
        
        else:
            j = m

    if A[i] != i: return i

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