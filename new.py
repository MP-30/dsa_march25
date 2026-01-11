arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]
b = 2

def solve(arr):
    n = len(arr)
    m = len(arr[0])
    for col in range(m-1,-1,-1):
        j = col
        i = 0
        while i < n and j >=0:
            print(arr[i][j], end=" ")
            i +=1
            j -=1
        print()
    for row in range(1,n):
        i = row
        j = m-1
        while j >=0 and i <n:
            print(arr[i][j],end=' ')
            i +=1
            j -=1
        print()
    
print(solve(arr))


a = [2,3,4,5,6,7,1]