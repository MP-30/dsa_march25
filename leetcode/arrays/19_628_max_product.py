'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
Example 1:
Input: nums = [1,2,3]
Output: 6
Example 2:
Input: nums = [1,2,3,4]
Output: 24
Example 3:
Input: nums = [-1,-2,-3]
Output: -6
'''
nums = [-100,-98,-1,2,3,4]
def max_product(nums):
    sorted(nums)
    return (nums[-1] * nums[-2] * nums[-3])
print(max_product(nums))