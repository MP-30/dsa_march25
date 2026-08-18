def solve(mat):
    # right
    n = len(mat)
    right_sum = 0
    for i in range(0,n):
        right_sum += mat[i][i]
    
    left_sum = 0
    j = 0
    k = n-1
    while j < n and k >=0:
        if j != k:
            left_sum += mat[j][k]
        j +=1
        k -=1
    return right_sum + left_sum
    
mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]

print(solve(mat))