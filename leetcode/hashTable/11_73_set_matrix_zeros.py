def setZeroes(matrix):
    ...
    i_to_be_zeros = []
    j_to_be_zeros = []
    x_of_matrix = len(matrix)
    y_of_matrix = len(matrix[0])
    for i in range(x_of_matrix):
        for j in range(y_of_matrix):
            if matrix[i][j] == 0:
                i_to_be_zeros.append(i)
                j_to_be_zeros.append(j)
                
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if i in i_to_be_zeros or j in j_to_be_zeros:
                matrix[i][j] = 0

    return matrix
    
    
# def setZeroes(matrix):
#     i_to_be_zeros = []
#     j_to_be_zeros = []
#     x_of_matrix = len(matrix)
#     y_of_matrix = len(matrix[0])
#     for i in range(x_of_matrix):
#         for j in range(y_of_matrix):
#             if matrix[i][j] == 0:
#                 i_to_be_zeros.append(i)
#                 j_to_be_zeros.append(j)
                
#     i_to_be_zeros = list(set(i_to_be_zeros))
#     j_to_be_zeros = list(set(j_to_be_zeros))

#     for a in i_to_be_zeros:
#         for b in range(y_of_matrix):
#             matrix[a][b] = 0
#     for c in j_to_be_zeros:
#         for d in range(x_of_matrix):
#             matrix[d][c] = 0

#     return matrix    
    

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))