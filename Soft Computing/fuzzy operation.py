
def union(A, B):
    Y = dict()
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        max_value = max(A_value, B_value)
        Y[A_key] = max_value
        
    print('\nFuzzy Set Union is :', Y)

def intersection(A, B):
    Y = dict()
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        min_value = min(A_value, B_value)
        Y[A_key] = min_value
                    
    print('\nFuzzy Set Intersection is :', Y)

def complement(A):
    Y = dict()
    for A_key in A:
        Y[A_key] = 1 - A[A_key]

    print('\nInput Fuzzy Set is:', A)
    print('Its Complement is :', Y)

def difference(A,B):
    Y = dict()
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        min_value = min(A_value, round(1-B_value, 2))
        Y[A_key] = min_value

    print('\nFuzzy Set Difference is :', Y)


A = dict()
B = dict()

A = {"a": 0.2, "b": 0.3, "c": 0.5}
B = {"a": 0.8, "b": 0.6, "c": 0.3}

print('The First Fuzzy Set is :', A)
print('The Second Fuzzy Set is :', B)


print()
union(A,B)
intersection(A,B)
difference(A,B)
complement(A)

