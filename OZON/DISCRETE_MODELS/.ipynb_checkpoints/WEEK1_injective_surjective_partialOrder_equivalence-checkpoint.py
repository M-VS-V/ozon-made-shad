def is_function(R, A, B):
    left = set()
    right = set()
    for x in R:
        if x[0] in left or x[0] not in A or x[1] not in B:
            return False
        left.add(x[0])
    return left == A

def is_injective(R, A, B):
    left = set()
    right = set()
    for x in R:
        if x[1] in right or x[0] not in A or x[1] not in B:
            return False
        right.add(x[1])
    return True

def is_surjective(R, A, B):
    left = set()
    right = set()
    for x in R:
        if x[0] not in A or x[1] not in B:
            return False
        right.add(x[1])
    return right == B

from itertools import product
def is_partial_order(R, A):
    #Reflexivity
    for x in A:
        if (x, x) not in R:
            return False
    
    #Antisimmetrisity
    for x in R:
        a, b = x
        if a not in A or b not in A:
            return False
        if a != b and (b,a) in R:
            return False

    #Transitivity
    for tuplePairs in product(R,R):
        a, b = tuplePairs[0]
        c, d = tuplePairs[1]
        if b==c and (a, d) not in R:
            return False
    return True
    
def is_equivalence_relation(R, A):
    #Reflexivity
    for x in A:
        if (x, x) not in R:
            return False
    
    #Simmetrisity
    for x in R:
        a, b = x
        if a not in A or b not in A:
            return False
        if (b, a) not in R:
            return False

    #Transitivity
    for tuplePairs in product(R,R):
        a, b = tuplePairs[0]
        c, d = tuplePairs[1]
        if b == c and (a, d) not in R:
            return False
    return True

print(is_equivalence_relation({(1, 2), (3, 3), (4, 4), (1, 4), (2, 4), (2, 2), (3, 4), (1, 1)}, {1, 2, 3, 4}))

