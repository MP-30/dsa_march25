'''
Print boundary elements
'''

mtrx = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
def solve_Clock(mtrx):
    length = len(mtrx[0])
    result = []

    for i in range(length):
        result.append(mtrx[0][i])
    for j in range(1,length):
        result.append(mtrx[j][length-1])
    for k in range(length-2,-1,-1):
        result.append(mtrx[length-1][k])
    for l in range(length-2,0,-1):
        result.append(mtrx[l][0])
    return result

def solve_antiClock(mtrx):
    length = len(mtrx[0])
    result = []

    for i in range(length):
        result.append(mtrx[i][0])
    for j in range(1,length):
        result.append(mtrx[length-1][j])
    for k in range(length-2,-1,-1):
        result.append(mtrx[k][length-1])
    for l in range(length-2,0,-1):
        result.append(mtrx[0][l])
    return result


print(solve_Clock(mtrx))