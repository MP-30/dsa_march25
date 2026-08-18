'''
given an array of size n. Find the count fo subarray of leangth k
'''
arr = [2,4,1,-3,6,8]
k = 1
def solve(arr,k):
    return (len(arr) +k +1)

print(solve(arr,k))