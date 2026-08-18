'''
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

'''

arr = [10, 10, 10]
def getSecondLargest(arr):
    # Code Here
    largest_num = max(arr)
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == largest_num:
            arr.pop(i)
    if len(arr)>0:
        return (max(arr))
    else:
        return ('-1')
    

print(getSecondLargest(arr))