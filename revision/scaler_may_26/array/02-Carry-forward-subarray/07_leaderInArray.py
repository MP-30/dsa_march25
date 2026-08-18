A = [16, 17, 4, 3, 5, 2]
output = [17,2,5]

def solve(A):
    greater = float("-inf")
    result = []
    for i in range(len(A)-1,-1,-1):
        if A[i] > greater:
            result.append(A[i])
            greater = A[i]
    return  result

print(solve(A))
