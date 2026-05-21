A = [-7, 1, 5, 2, -4, 3, 0]
output = 3

def solve(A):
    left_prefix = [A[0]]
    right_prefix = [A[-1]]
    for i in range(1,len(A)):
        left_prefix.append(A[i]+ left_prefix[-1])
    for j in range(len(A)-2,-1,-1):
        right_prefix.append(A[j]+right_prefix[-1])

    for k in range(len(A)):
        if left_prefix[k] == right_prefix[(len(A)-1)-k]:
            return  k
    else: return  -1

print(solve(A))