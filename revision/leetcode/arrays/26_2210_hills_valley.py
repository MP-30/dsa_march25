def check1(nums):
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            nums.pop(i-1)
    print(nums)
        
    valley = 0
    hills = 0
    if len(nums) >2:
        for i in range(1,len(nums)-1):
                if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                    hills +=1
                elif nums[i-1] > nums[i] and nums[i+1] > nums[i]:
                    valley +=1
    return valley+ hills


def check(nums):
    new_arr = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            new_arr.append(nums[i])
        
    valley = 0
    hills = 0
    if len(new_arr) >2:
        for i in range(1,len(new_arr)-1):
                if new_arr[i-1] < new_arr[i] and new_arr[i+1] < new_arr[i]:
                    hills +=1
                elif new_arr[i-1] > new_arr[i] and new_arr[i+1] > new_arr[i]:
                    valley +=1
    return valley+ hills

# nums = [2,4,1,1,6,5]
# nums = [6,6,5,5,4,1]
nums = [44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,40,40]
print(check(nums))