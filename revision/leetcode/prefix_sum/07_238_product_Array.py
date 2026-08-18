def solve(arr):
    result = []
    prefix_fwd = [1]
    prefix_back = [1]
    for i in range(0,len(arr)-1):
        prefix_fwd.append(prefix_fwd[-1] * arr[i])
    for i in range(len(arr)-1,0,-1):
        prefix_back.append(prefix_back[-1] * arr[i])
    for i in range(len(arr)):
        result.append(prefix_fwd[i] * prefix_back[-(i+1)])
    return result
    ...
    
# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(solve(nums))