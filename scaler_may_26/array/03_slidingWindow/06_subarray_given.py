A = [6,3,3,6,7,8,7,3,7]
B = 2
C = 10
output = 1
def solve(A,B,C):
    summ = sum(A[:B])
    if summ == C:
        return 1
    j = 0
    for i in range(B, len(A)):
        new_sum = summ - A[j] + A[i]
        summ = new_sum
        print(new_sum)
        if new_sum == C:
            return  1
        j +=1
    return 0
print(solve(A,B,C))