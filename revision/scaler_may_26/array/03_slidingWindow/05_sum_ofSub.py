A = [2, 1, 3]
output = 19

def solve(A):
    result = 0
    for i in range(len(A)):
        result += A[i] * (i +1) * (len(A) -i)

    return result
print(solve(A))