'''
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
[1, 2, 0, 4, 3, 0, 5, 0]
'''
# arr = [3, 5, 0, 0, 4]
arr = [1, 2, 0, 4, 3, 0, 5, 0]
# arr = [[0, 0]]
# def move_zeros(arr):
#     result = []
#     count = 0
#     for i in arr:
#         if i == 0:
#             count +=1
#         elif i != 0:
#             result.append(i)
#     for j in range(0,count):
#         result.append(0)
#     return(result)
    

# def move_zeros(arr):
#     for i in range(len(arr)-1,-1,-1):
#         if arr[i] == 0:
#             arr.append(arr[i])
#             arr.pop(i)
#     print(arr)


# for i in range(0,len(arr)):
#     if arr[i] == 0:
#         arr[i],arr[-1] = arr[-1], arr[i]
# print(arr)

# for i in range(0,len(arr)):
#         if arr[i] == 0:
#             for j in range(i+1, len(arr)):
#                 if arr[j] != 0:
#                     arr[i], arr[j] = arr[j], arr[i]
#                     break
#     return(arr)
    


# for i in range(0,len(arr)):
#         if arr[i] == 0:
#             start_range = i+1
#             for j in range(start_range, len(arr)):
#                 if arr[j] != 0:
#                     start_range = j
#                     arr[i], arr[j] = arr[j], arr[i]
#                     break
#     return(arr)


def move_zeros(arr):
    count = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i],arr[count]
            count+=1
    return arr


print(move_zeros(arr))



[1, 2, 0, 4, 3, 0, 5, 0]