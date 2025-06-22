# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]

def remove_duplicate(nums):
    temp_arr = {}
    for i in range(len(nums)-1,-1,-1):
        if nums[i] in temp_arr:
            nums.pop(i)
        else:
            temp_arr[nums[i]] = 1
    print(len(nums))
    
remove_duplicate(nums)