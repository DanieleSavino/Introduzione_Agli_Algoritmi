class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

    @classmethod
    def fromArray(cls, A):
        if len(A) < 1: return None

        P = Q = cls(A[0])
        for i in range(1, len(A)):
            P.next = Node(A[i])
            P = P.next

        return Q
    
    def __repr__(self):
        A = []
        P = self
        while P != None:
            A.append(f'{P.key}')
            A.append(' --> ')
            P = P.next
        A.append('None')
        return ''.join(A)