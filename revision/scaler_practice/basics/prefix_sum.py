'''
Given an array of N element. Find the 
maximum subarray sum for subarray with length R.
'''


def solve(A,B):
    average = sum(A[:B])
    min_avg = average
    print(A[:B])
    index_value = 0
    i = 0
    j = B
    while j < len(A):
        average = average - A[i]
        average += A[j]
        if average < min_avg:
            min_avg = average
            index_value = i +1
        j +=1
        i +=1
    return index_value
    
# A = [3,7,90,20,10,50,40]
A = [15,3,15,6,9,14,8,10,9,17]
# B = 3
B = 1
print(solve(A,B))
