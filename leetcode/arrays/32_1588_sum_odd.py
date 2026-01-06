def sum_odd(arr):
    prefix = [0]
    for i in arr:
        prefix.append(prefix[-1] + i)
    total_sum = 0
    for i in range(0,len(arr)):
        for j in range(i,len(arr),2):
            total_sum += prefix[j+1]-prefix [i]
    return total_sum
    ...
    
arr = [10,11,12]
# print(sum_odd(arr))

a = [9,2,3,4,2,4,8]
prefix_min = [a[0]]
for i in a:
    prefix_min.append(min(prefix_min[-1],  i))
print(prefix_min)
# next greater element 
# next lesser element