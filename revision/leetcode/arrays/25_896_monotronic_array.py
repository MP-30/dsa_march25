def monotonic1(nums):
    def increasing():
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    def decreasing():
        for i in range(0,len(nums)-1):
            if nums[i] < nums[i+1]:
                return False
        return True
        
    if len(nums) < 3 :
        return True
    elif len(nums) >= 3 :
        first = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < first:
                result = decreasing()
                return result
            elif nums[i] > first:
                result = increasing()
                return result
         
        return True   
    else:
        return True
    

def monotonic2(nums):
    inc = dec = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            inc = False
        if nums[i] < nums[i+1]:
            dec = False
    return inc or dec

def monotonic(nums):
    inc = dec = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            inc = False
        if nums[i] < nums[i+1]:
            dec = False
            
        if not inc and not dec:
            return False
        
    return True

    
# nums = [1,2,2,3]
# nums = [6,5,4,4]
# nums = [1,3,2]
# nums =[1,1,1]
nums = [1, 1, 1, 0]

print(monotonic(nums))