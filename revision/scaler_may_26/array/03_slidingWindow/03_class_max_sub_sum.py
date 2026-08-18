'''
Given an array of N elements. Find the maximun subarray sum for subarray with length k
'''
# arr = [-3,4,-2,5,3,-2,8,2,-1,4]
# k = 5
arr = [1,2,3,4,5]
k = 2

def solve(arr,k):
    base_sum = sum(arr[:k])
    max_sum = base_sum
    for i in range(0,len(arr)-k):
        base_sum = base_sum + arr[i+(k)] - arr[i]
        max_sum = max(base_sum, max_sum)
    return max_sum
print(solve(arr,k))