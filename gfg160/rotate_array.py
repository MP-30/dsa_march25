'''
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
'''

arr = [1,2,3,4,5]
d = 2
def arr_rotate(arr,d):
    return (arr[d:] + arr[:d])
print(arr_rotate(arr,d))