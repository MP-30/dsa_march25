arr = [-5,1,2,3,2]

def solve(arr):
    result = [arr[0]]
    for i in range(1,len(arr)):
        result.append(max(result[-1], arr[i]))
    print(result)
    result1 = [0] * len(arr)
    last_max = arr[-1]
    for j in range (len(arr)-1,-1,-1):
        result1[j] = (max(last_max, arr[j]))
        last_max = (max(last_max, arr[j]))
    print(result1)

print(solve(arr))