'''Given an integer array A, find the maximum subarray sum out of all the subarrays'''

A = [-1,4,6,2,8,-2,3]







# kedan algo

def solve(a):
    max_sum = float('-inf')
    current_sum = float('-inf')
    for i in range(len(a)):
        current_sum = max(current_sum + a[i], a[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


# kedane algo for finding sum

# def solve(a):
#     summ = []
#     max_sum = float('-inf')
#     current_sum = float('-inf')
#     for i in range(len(a)):
#
#         if a[i] < current_sum + a[i]:
#             current_sum += a[i]
#         else:
#             current_sum = a[i]
#         summ.append(current_sum)
#         max_sum = max(max_sum, current_sum)
#     print(summ)
#     print(max_sum)


# def solve(A):
#     max_sum = float('-inf')
#     pre_fix = [0]
#     for k in range(0,len(A)):
#         pre_fix.append(pre_fix[-1] + A[k])
#     for i in range(len(A)):
#         for j in range(i,len(A)):
#             max_sum = max(max_sum, pre_fix[j+1]-pre_fix[i])
#     print(pre_fix)
#     return  max_sum


print(solve(A))
