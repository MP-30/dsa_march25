'''
Given an array find the length of smallest 
subarray which contains both min and max of array.
'''


def solve(A,B):
    left = 0
    sum = 0
    right = 0
    count = 0
    while right < len(A):
        sum += A[right]
        while sum >= B and left <=right:
            sum -= A[left]
            left +=1
        count += right - left +1
        right +=1
    return count

a = [1,11,2,3,15]
b = 10
c = [1,12,14,17,32]
print(solve(a,b))
