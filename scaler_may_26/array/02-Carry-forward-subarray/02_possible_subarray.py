'''print all possible sub array'''

arr = [1,2,3]
def solve(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            result.append(arr[i:j+1])
    return  result

print(solve((arr)))