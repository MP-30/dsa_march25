arr = [[1,2,3],[4,5,6],[7,8,9]]

def solve(arr):
    result = []
    for i in range(len(arr[0])):
        row = 0
        col = i
        dd = [] 
        while row < len(arr) and col >=0:
            dd.append(arr[row][col])
            row +=1
            col -=1
        while len(dd)< len(arr):
            dd.append(0)
        result.append(dd)
    for j in range(1,len(arr)):
        dd = []
        row = j
        col = len(arr)-1
        while row < len(arr) and col >=0:
            dd.append(arr[row][col])
            row +=1
            col -=1
        while len(dd)< len(arr):
            dd.append(0)
        result.append(dd)
        
    return result    
    ...
        
print(solve(arr))
