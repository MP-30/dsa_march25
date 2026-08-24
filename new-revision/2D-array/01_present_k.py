'''
Given a row wise and column wise sorted matrix,
find out whether element k is present or not.
'''

# A = [[-5,-2,1,13],
#      [-4,0,3,14],
#      [-3,2,6,18]]


# case = 13
case = 2
# case = 15

def solve(A,case):
    if not A or not A[0]:
        return False
    i = 0
    j = len(A)-1
    while i < len(A[0]) and j >=0:
        if A[i][j] == case:
            return True
        elif A[i][j] < case:
            i +=1
        else:
            j -=1

    return False



def solve2(A,case):
     possible_colunm = []
     possible_row = []
     row_length = len(A[0])
     column_length = len(A)
     for i in range(column_length):
         if case >= A[i][0] and case <= A[i][row_length-1]:
             possible_row.append(i)
     for j in range(row_length):
         if case >= A[0][j] and case <= A[column_length-1][j]:
             possible_colunm.append(j)
     if len(possible_row) ==0 or len(possible_colunm) == 0:
         return False
     else:
         for k in possible_colunm:
             for l in range(column_length):
                if A[l][k] == case:
                    return True
         for m in possible_row:
             for n in range(row_length):
                if A[m][n] == case:
                    return True
     return False


def solve1(A,case):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == case:
                return True
    else: return False

print(solve(A,case))