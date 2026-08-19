'''
Given an integer array A such that all the elements in the array are 0. Return the final array
after performing multiple queries Query: (i,j,x): Add x to all elements from index i to j
Given that i <= j
E.g.
q1 = (1,3,2)
q2 = (2,5,3)
q3 = (5,6,-1)
'''
q = ( (1,3,2), (2,5,3), (5,6,-1))
a = [0,0,0,0,0,0,0]
ans = [0, 2, 5, 5, 3, 2, -1]
def solve(a,q):
    for i in q:
        start, end, x = i
        a[start] += x
        if end +1 < len(a):
            a[end +1 ] -= x

    for j in range(1,len(a)):
        a[j] += a[j-1]
    return a

# def solve1(a,q):
#     for i in q:
#         for j in range(i[0], i[1]+1):
#             a[j] += i[2]
#     return a

print(solve(a,q))