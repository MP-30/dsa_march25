'''
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.
'''
# A = [ [1, 2,3], [4, 5,6],[6,7,8] ]
A = [[8,9,9,1,7],[5,5,10,1,0],[7,7,5,8,6],[7,3,7,9,2],[7,7,8,10,6]]
def solve(A):
    summ = 0
    sum_matrix = []
    for i in range(len(A)):
        for j in range(len(A)):
            sum_matrix.append([i,j])
    for a,b in sum_matrix:
        for j in range(a,len(A)):
            for k in range(b,len(A)):
                summ += A[j][k]
    return(summ)


print (solve(A))