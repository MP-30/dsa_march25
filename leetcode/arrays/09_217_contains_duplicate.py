'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
'''
nums: list = [2,14,18,22,22]
def contains_duplicate(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            dic[i]+=1
    print(dic)
    for j in dic.values():
        if j >1:
            return True 
    return False

'''

nums: list = [2,14,18,22,22]
def contains_duplicate(nums):
    dic = {}
    for i in nums:
        if i in dic:
            return True
        dic[i] = 1
    return False
print(contains_duplicate(nums))