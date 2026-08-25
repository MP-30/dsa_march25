'''
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.
'''
# A = 1
# A = 2
A = 5
def solve(A):
    top = 0
    left = 0
    right = A
    bottom = A

    mtrix = [[0 for _ in range(A)] for _ in range(A)]
    value = 0
    while top <= bottom-1 and left <= right-1:
        # for top
        for i in range(left,right):
            value +=1
            mtrix[top][i] = value
        # for right
        for j in range(top+1, bottom):
            value +=1
            mtrix[j][right-1] = value
        # for bottom
        if top <= bottom-1:
            for k in range(right-1-1, left-1,-1):
                value +=1
                mtrix[bottom-1][k] = value
        # for left
        if left <= bottom-1:
            for l in range(bottom-1-1, top,-1):
                value +=1
                mtrix[l][left] = value
        top +=1
        left +=1
        right -=1
        bottom -=1
    return(mtrix)

print(solve(A))