'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
'''
# nums = [1,2,2,3,1,4,2]
nums = [1,2,2,3,1]
def degree(nums):
    counter = {}
    for i in nums:
        if i not in counter:
            counter[i] = 1
        elif i in counter:
            counter[i] +=1
    max_degree = max(counter.values())
    all_max_degree_key = []
    for k,l in counter.items():
        if l == max_degree:
            all_max_degree_key.append(k)
    sub_array = {}
    for i in range(0,len(nums)):
        if nums[i] in all_max_degree_key:
            if nums[i] not in sub_array:
                sub_array[nums[i]] = [i]
            elif nums[i] in sub_array:
                sub_array[nums[i]].append(i)
    min_required_steek = 100000000000
    for a in sub_array.values():
        if abs(a[0] - a[-1]) +1 < min_required_steek:
            min_required_steek = abs(a[0] - a[-1]) +1
    return(min_required_steek)
      
        
degree(nums)