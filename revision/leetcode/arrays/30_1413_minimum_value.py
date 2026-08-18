def minimum(nums):
    startValue = 0
    result = False
    while result == False:
        prefix_sum = []
        startValue +=1
        for i in range(0,len(nums)):
            if i == 0:
                if startValue + nums[i] >0:
                    prefix_sum.append(startValue + nums[i])
              
            else:
                if prefix_sum[-1] + nums[i] >0:
                    prefix_sum.append(prefix_sum[-1] + nums[i])
        
        if len(prefix_sum) == len(nums):
            return startValue
    
# nums = [-3,2,-3,4,2]
# nums = [1,2]
# nums = [1,-2,-3]
nums = [-12]
print(minimum(nums))