'''
Gicen an array of a interger, the objectice is to minimize the total cost of emptying the array. The cost
of removing an element is definied as the sum of all remaining elements in the array at the
time of removal.
'''

a = [2,1,4]
ans = 11
def solve(a):
    a = sorted(a)
    for i in range(len(a)-1,-1,-1):
        print(a[i])
        a.pop(i)

print(solve(a))