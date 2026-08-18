'''
you are given an array of integers arr[]. Your task is to reverse the given array. 
Note: Modify the array in place
'''

arr = [1,4,3,2,6,5]

def reverse_Arr(arr):
    for i in range(0,(len(arr)//2)):
        arr[i],arr[-(i+1)] = arr[-(i+1)],arr[i]
    print(arr)
    
reverse_Arr(arr)