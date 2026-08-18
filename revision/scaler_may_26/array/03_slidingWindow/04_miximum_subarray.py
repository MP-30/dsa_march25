A = 5
B = 12
C = [2, 1, 3, 4, 5]
output = 12

def solve(A,B,C):
    result = float('-inf')
    i = 0
    while i < A:
        local_sum = 0
        j = i
        while j < A:
            local_sum += C[j]
            if local_sum > result and local_sum <= B:
                result = local_sum
            j +=1
        i +=1
    if result != float('-inf'):
        return  result
    else:
        return 0

print(solve(A,B,C))