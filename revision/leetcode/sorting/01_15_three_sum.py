def three_sum(nums):
    ...
    first_result = []
    main_result = []
    length = len(nums)
    for i in range(length):
        for j in range(length):
            to_add = list(set([i,j]))
            if i != j and to_add not in first_result:
                first_result.append(to_add)
    
    for k in first_result:
        for l in range(length):
            if l not in k:
                if nums[k[0]] + nums[k[1]] + nums[l] == 0:
                    main_result.append([nums[k[0]] + nums[k[1]] + nums[l]])
    
    
    return main_result

input = [-1,0,1,2,-1,-4]
# input = [0,0,0]

print(three_sum(input))

a = [{0, 1}, {0, 2}, {0, 3}, {0, 4}, {0, 5}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 3}, {2, 4}, {2, 5}, {3, 4}, {3, 5}, {4, 5}]