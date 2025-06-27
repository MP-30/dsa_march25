m =39999
n =39999
ops =[[19999,19999]]
Output: 4

def operations(m,n,ops):
    if not ops:
        return m*n
    min_a = min (op[0] for op in ops)
    min_b = min (op[1] for op in ops)
    return min_a * min_b
print(operations(m,n,ops))