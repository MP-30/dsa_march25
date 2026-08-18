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
    negative_nums = []
    positive_nums = []
    all_max = []
    for i in nums:
        if i >= 0:
            positive_nums.append(i)
        else: negative_nums.append(i)
    sorted_negative = sorted(negative_nums)
    sorted_positive = sorted(positive_nums)
    if len(positive_nums)>2:
        all_positive = sorted_positive[-1] * sorted_positive[-2] * sorted_positive[-3]
        all_max.append(all_positive)
    if len(negative_nums)> 2:
        all_negative = sorted_negative[-1] * sorted_negative[-2] * sorted_negative[-3]
        all_max.append(all_negative)
    if len(negative_nums)>1  and len(positive_nums)> 0:
        two_negative = sorted_positive[-1] * sorted_negative[0] * sorted_negative[1]    
        all_max.append(two_negative)
    print(f"negative_nums {sorted_negative} , positive_num {sorted_positive}")
    print(all_max)
    return(max(all_max))
print(max_product(nums))



















# def max_product(nums):
#     nums1 = (sorted(nums))
#     max_positive = nums1[-1]
#     two_max_positive = nums1[-3:-1]
#     two_max_negative = []
#     if nums1[0] < 0:
#         two_max_negative.append(nums1[0])
#     if nums1[1] < 0:
#         two_max_negative.append(nums1[1])
#     positive_mul = two_max_positive[0] * two_max_positive[1]
#     print(two_max_negative)
#     print(two_max_positive)
#     print(nums1)
#     if len(two_max_negative) == 2:
#         negative_mul = two_max_negative[0] * two_max_negative[1]
#         if negative_mul > positive_mul:
#             return max_positive * negative_mul
#         else:
#             return max_positive * positive_mul
#     else:
#         return max_positive * positive_mul
    
# print(max_product(nums))