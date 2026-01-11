def solve(nums):
    prefix_even = [0]
    prefix_odd = [0]
    for i in range(len(nums)):
        if i % 2 == 0:
            prefix_even.append(prefix_even[-1]+ nums[i])
        elif i % 2 != 0:
            prefix_odd.append(prefix_odd[-1] + nums[i])
    total_even = prefix_even[-1]
    total_odd = prefix_odd[-1]
    count = 0
    even_before = 0
    odd_before = 0
    
    for i , val in enumerate(nums):
        if i % 2 ==0:
            total_even -= val
        else:
            total_odd -= val
        
        if even_before + total_odd == odd_before + total_even:
            count +=1
            
        if i % 2 ==0:
            even_before += val
        else:
            odd_before += val

    return count
        
arr = [1,2,3,4,1,2,3]
print(solve(arr))