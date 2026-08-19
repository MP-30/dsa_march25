'''
given an integer array A where every element is 0, return the final array after performing multiple queries.
Query(i,x): Add x to all the numbers from index i to N-1
Example
Query (1,3)
Query (4,-2)
Query(3,1)
'''
a = [0,0,0,0,0,0,0]
q = ( (1,3), (4,-2), (3,1))

def solve(a, q):
    length = len(a)
    for i in q:
        a[i[0]] += i[1]
    for j in range(1,length):
        a[j] = a[j-1] + a[j]
    return(a)

# def solve1(a, q1,q2,q3):
#     result = a
#     for i in (q1,q2,q3):
#         for j in range(i[0],len(a)):
#             result[j] += i[1]
#     return result

print(solve(a,q))