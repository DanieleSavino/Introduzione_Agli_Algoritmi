from random import randint

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    @classmethod
    def fromArray(cls, A, index=0):
        if index < len(A):
            if A[index] is None:
                return None
            else:
                node = cls(A[index])
                node.left = cls.fromArray(A, 2 * index + 1)
                node.right = cls.fromArray(A, 2 * index + 2)
                return node
        else:
            return None
        
    @classmethod
    def randomTree(cls, length, min_key, max_key, balanced=False):
        A = []
        for _ in range(length):  
            A.append(randint(min_key, max_key) if balanced or randint(0, 10) < 8 else None)

        return cls.fromArray(A)
        
    def __repr__(self):
        return self._repr_helper(self, "", True, [])

    def _repr_helper(self, node, prefix, is_left, out):
        if node is None:
            return

        self._repr_helper(node.right, prefix + ("│   " if is_left else "    "), False, out)
        out.append(prefix + ("└── " if is_left else "┌── ") + str(node.key))
        self._repr_helper(node.left, prefix + ("    " if is_left else "│   "), True, out)

        return '\n'.join(out)