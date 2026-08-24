'''
Print boundary elements
'''

# mtrx = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# mtrx = [[1,2,3],[4,5,6],[7,8,9]]
mtrx = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def solve_Clock(mtrx):
    if not mtrx:
        return []
    length_row = len(mtrx)
    length_col = len(mtrx[0])
    result = []
    top = 0
    left = 0
    right = length_col-1
    bottom = length_row-1

    while top <= bottom and left <= right:
        for i in range(left,right +1):
            result.append(mtrx[top][i])
        top += 1
        for j in range(top,bottom+1):
            result.append(mtrx[j][right])
        right -= 1

        if top <= bottom:
            for k in range(right,left -1 ,-1):
                result.append(mtrx[bottom][k])
            bottom -= 1
        if left <= right:
            for l in range(bottom,top-1,-1):
                result.append(mtrx[l][left])
            left += 1
        print (top, left, right, bottom)

    return result



print(solve_Clock(mtrx))