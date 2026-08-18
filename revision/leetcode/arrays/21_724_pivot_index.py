nums = [-1,-1,0,1,1,0]



def pivot(nums):
    if len(nums)>1:
        sum_of_left = 0
        sum_of_right = sum(nums[1:])
        for i in range(1,len(nums)):
            if sum_of_left != sum_of_right:
                sum_of_left += nums[i-1]
                sum_of_right -= nums[i]
                print(f"right {sum_of_right} and left {sum_of_left} and i is {i}")
                if sum_of_left == sum_of_right:
                    return (i)
            elif sum_of_left == sum_of_right:
                return (i-1)
        return (-1)
    elif len(nums) == 1:
        return (0)
    else: return (-1)
print(pivot(nums))



# def pivot(nums):
#     if len(nums)>3:
#         sum_of_left = 0
#         sum_of_right = sum(nums[1:])
#         for i in range(1,len(nums)):
#             if sum_of_left != sum_of_right:
#                 sum_of_left += nums[i-1]
#                 sum_of_right -= nums[i]
#                 print(f"right {sum_of_right} and left {sum_of_left} and i is {i}")
#                 if sum_of_left == sum_of_right:
#                     return (i)
#             elif sum_of_left == sum_of_right:
#                 return (i-1)
#         return (-1)
#     elif len(nums) == 1:
#         return (0)
#     elif len(nums) == 2:
#         if nums[0] == 0:
#             return (1)
#         elif nums[1] == 0:
#             return (0)
#         else: return (-1)
#     elif len(nums) == 3:
#         if nums[0] == nums[-1]:
#             return(1)
#         elif sum(nums[:2]) == 0:
#             return(2)
#         elif sum(nums[1:]) == 0:
#             return (0)
#         else: return (-1)
#     else: return (-1)
# print(pivot(nums))