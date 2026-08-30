'''
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.
'''
# A = [ [1, 2,3], [4, 5,6],[7,8,9] ]
A = [[8,9,9,1,7],
     [5,5,10,1,0],
     [7,7,5,8,6],
     [7,3,7,9,2],
     [7,7,8,10,6]]
def solve(A):
    n = len(A)
    total = 0
    for i in range(n):
        for j in range(n):
            count = (i +1) * (j +1) * (n-i) * ( n - j)
            total += A[i][j] * count
    return total


print (solve(A))



