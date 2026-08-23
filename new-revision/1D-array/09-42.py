# A = [5, 4, 1, 4, 3, 2, 7]
A = [1,0,2,5,1,0,3,0,0,7]

def solve(A):
    right = [0] * len(A)
    left = [0] * len(A)
    maxx = 0
    minn = 0
    water = 0
    for i in range(len(A)-1,-1,-1):
        if A[i] > maxx:
            right[i] = A[i]
            maxx = A[i]
        else:
            right[i] = maxx
    for j in range(len(A)):
        if A[j] > minn:
            left[j] = A[j]
            minn = A[j]
        else:
            left[j] = minn

    for k in range(len(A)):
        water += min ( left[k], right[k]) - A[k]

    return water
print(solve(A))
