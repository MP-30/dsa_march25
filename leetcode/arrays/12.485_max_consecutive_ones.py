nums = [1,1,0,1,1,1]

def max_consecutive(nums):
    max_counter = 0
    local_max_counter = 0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            local_max_counter +=1
            if local_max_counter > max_counter:
                max_counter = local_max_counter
        elif nums[i] != 1:
            local_max_counter =0
    return max_counter

print(max_consecutive(nums))
                