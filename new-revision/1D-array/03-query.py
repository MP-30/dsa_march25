'''
given an integer array A where every element is 0, return the final array after performing multiple queries.
Query(i,x): Add x to all the numbers from index i to N-1
Example
Query (1,3)
Query (4,-2)
Query(3,1)
'''
a = [0,0,0,0,0,0,0]
Query1 = (1,3)
Query2 = (4,-2)
Query3 = (3,1)

def solve(a, q1,q2,q3):
    result = a
    for i in (q1,q2,q3):
        for j in range(i[0],len(a)):
            result[j] += i[1]
    return result

print(solve(a,Query1,Query2,Query3))