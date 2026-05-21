'''given an array find the length of smallest subarray which contains both
min and max of array'''

arr = [1,2,3,1,3,4,6,4,6,3]
def solve0(arr):
    minn = min(arr)
    maxx = max(arr)
    if minn == maxx:
        return  1
    min_index = []
    max_index = []
    for i in range(len(arr)):
        if arr[i] == minn:
            min_index.append(i)
        elif arr[i] == maxx:
            max_index.append(i)
    result = float("inf")
    for j in min_index:
        for k in max_index:
            if abs(j-k) +1 < result:
                result = abs(j-k) +1
    return  result

def solve(arr):
    minn = min(arr)
    maxx = max(arr)
    if minn == maxx:
        return  1
    min_index = -1
    max_index = -1
    count = len(arr)
    for i in range(len(arr)):
        if arr[i] == minn:
            min_index = i
            if max_index >=0 and abs(min_index - max_index)+1 < count:
                count = abs(min_index - max_index)+1
        elif arr[i] == maxx:
            max_index = i
            if min_index >=0 and abs(min_index - max_index)+1 < count:
                count = abs(min_index - max_index)+1

    return  count

print(solve(arr))