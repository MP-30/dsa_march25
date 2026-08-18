def check(nums):
    dictt = {}
    for i in nums:
        if i in dictt:
            return i
        elif i not in dictt:
            dictt[i] = 1
    
        
    
    
nums = [5,1,5,2,5,3,5,4]
print(check(nums))