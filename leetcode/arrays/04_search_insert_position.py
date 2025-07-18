'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
nums = [1,3,5,6]
target = 7
def search_insert_positions(nums,target):
    if nums[-1] < target:
        return (len(nums))
    for i in range(0,len(nums)):
        if nums[i] > target or nums[i] == target:
            return (i)
        
        
print(search_insert_positions(nums, target))