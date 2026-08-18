# def find_difference(values,k):
#     if len(values)<2:
#         return False
#     else:
#         for i in range(0,len(values)):
#             # print(f"this is i {values[i]}")
#             for j in range(i+1,len(values)):
#                 # print(f"this is j {values[j]}")
#                 if abs(values[i]-values[j]) <=k:
#                     # print(f"diff {abs(values[i]-values[j])}")
#                     return True
#         return False

# def containsNearbyDuplicate(nums,k):
#     dt = {}
#     for i in range(0,len(nums)):
#         if nums[i] in dt:
#             dt[nums[i]].append(i)
#         else : dt[nums[i]] = [i]
#     # print(dt)
    
#     for j in dt.values():
#         a = find_difference(j,k)
#         if a == True:
#             return True
#     return False
    
# nums = [99,99]
# k=2
# print(containsNearbyDuplicate(nums,k))

def contain(nums,k):
    last_seen = {}
    for i , num in enumerate(nums):
        
    
nums = [99,99]
k=2

print(contain(nums,k))