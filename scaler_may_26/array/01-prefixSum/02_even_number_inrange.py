A = [1, 2, 3, 4, 5]
B = [ [0, 2] , [2, 4] , [1, 4] ]

def solve(A, B):
    pre_sum = [0]
    for i in range(len(A)):
        if A[i] % 2 == 0:
            pre_sum.append(1+ pre_sum[-1])
        else:
            pre_sum.append((pre_sum[-1]))

    result = []
    for a,b in B:
        result.append(pre_sum[b+1]-pre_sum[a])
    return  result

print((solve(A,B)))