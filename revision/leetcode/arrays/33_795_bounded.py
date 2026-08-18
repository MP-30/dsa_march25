def solve(nums, left, right):
    answer = 0
    count_elements = 0
    for i in range(0,len(nums)):
        if nums[i] <= right:
            count_elements +=1
        else:
            answer += (count_elements * (count_elements +1))/2
            count_elements = 0
    left_answer = 0
    left_count_element = 0
    for i in range(len(nums)):
        if nums[i]<=left-1:
            left_count_element +=1
        else:
            left_answer += (left_count_element * (left_count_element+1))/2
            left_count_element = 0
    result = answer - left_answer
    return result 
    
nums = [2,9,2,5,6]
left = 2 
right = 8
print(solve(nums,left,right))