'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
'''
nums = [3,2,1,4,1,5]
def third_maximun(nums):
    nums = set(nums)
    nums = sorted(nums, reverse=True)
    print(nums)
    if len(nums)>2:
        return(nums[2])
    else: return(max(nums))
third_maximun(nums)