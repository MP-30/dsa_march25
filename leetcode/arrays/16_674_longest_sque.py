nums = [1,3,5,7]

def longest(nums):
    if not nums:
        return 0
    
    max_stek = 1
    current_stek = 1
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            current_stek +=1
            max_stek = max(current_stek, max_stek)
        else:
            current_stek = 1
            
    return max_stek
print(longest(nums))