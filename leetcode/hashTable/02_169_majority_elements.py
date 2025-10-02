def check(nums):
    dictt = {}
    for i in nums:
        if i in dictt.keys():
            dictt[i] +=1
        else: dictt[i] =1
    maxx_value = float('-inf')
    maxx_int = 0
    for j,k in dictt.items():
        if k > maxx_value:
            maxx_value = k
            maxx_int = j
    return(maxx_int)
    
    
nums = [2,2,1,1,1,2,2]
check(nums)