A = [1, 2, 3, 4, 5]
output = [1,3,6,10,15]

def solve(A):
    for i in range(1,len(A)):
        A[i] = A[i-1] + A[i]
    return A

print(solve(A))