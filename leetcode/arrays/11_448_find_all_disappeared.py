'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
'''
# nums = [4,3,2,7,8,2,3,1]
nums =[1,1]
# def find_disappeared(nums):
#     result = []
#     new_nums = set(nums)
#     for i in range(1,len(nums)+1):
#         if i not in new_nums:
#             result.append(i)
#     return result
# print(find_disappeared(nums))
def find_disappeared(nums):
    result = []
    new_nums = sorted(nums)
    for i in range(1,len(new_nums)+1):
        if i not in new_nums:
            result.append(i)
    return result
print(find_disappeared(nums))