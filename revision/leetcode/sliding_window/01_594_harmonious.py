from collections import defaultdict, Counter
def solve(nums):
    dictt = defaultdict(int)
    for i in nums:
        dictt[i] +=1
    count_global = 0
    for i in dictt.keys():
        if i +1 in dictt.keys():
            count_global = max(count_global, dictt[i]+ dictt[i+1])
    return(count_global)
                
    
nums = [1,3,2,2,5,2,3,7]
print(solve(nums))