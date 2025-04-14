# Add two Matrices
# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]



def add_two(X,Y):
    result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

    for i in range(0,len(X)):
        for j in range(len(X[0])):
        # for j in range(0,i+1):
            result[i][j] = X[i][j] + Y[i][j]
    print (result)


# Multiply two matrices
a  = [[1,2],
      [3,4]]
b = [[4,5],
     [6,7]]


def mul_two(a,b):
    result = [[0,0],
            [0,0]]
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            result[i][j] = 0



# Matrix Product
# Adding and Subtracting Matrices
# Transpose a matrix in Single line
# Matrix creation of n*n
# Get Kth Column of Matrix
# Vertical Concatenation in Matrix



if __name__ == '__main__':
    # add_two(X,Y)
    mul_two(a,b)
    pass