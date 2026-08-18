def solve(nums):
    prefix = [0]
    for i in nums:
        prefix.append(prefix[-1]+ i)
    
    for i in range(1,len(prefix)-1):
        if prefix[i-1] == prefix[i] - prefix[i-1]:
            return i
    return -1
    
    
nums = [2,3,-1,8,4]
# nums = [1,-1,4]
print(solve(nums))