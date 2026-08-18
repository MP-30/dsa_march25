'''
Given an array of distinct elements of size n, find the count of noble integers.
arr[i] is noble if count of elements smaller then arr[i] is equal to arr[i], where arr[i] is
element at index i
'''
a =[ 1,-5,3,5,-10,4]
ans = 3

def solve(a):
    a = sorted(a)
    noble = 0
    for i in range(len(a)):
        if i == a[i]:
            noble +=1

    return  noble

print(solve(a))