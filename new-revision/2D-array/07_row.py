'''
Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.
NOTE:
If two rows have the maximum number of 1 then return the row which has a lower index.
Rows are numbered from top to bottom and columns are numbered from left to right.
Assume 0-based indexing.
Assume each row to be sorted by values.
Expected time complexity is O(rows + columns).
'''
A = [   [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 1]    ]
# A = [[0, 1, 1],
#      [0, 0, 1],
#      [0, 1, 1]]

def solve(A):
    rows = len(A)
    cols = len(A[0])
    row = 0
    col = cols -1
    result = 0
    while row < rows and col >= 0:
        if A[row][col] == 1:
            result = row
            col -=1
        else:
            row +=1
    return result

def solve1(A):
    result = 0
    maxx = 0
    for i in range(len(A)):
        if sum(A[i]) > maxx:
            maxx = sum(A[i])
            result = i
    return result

print(solve(A))