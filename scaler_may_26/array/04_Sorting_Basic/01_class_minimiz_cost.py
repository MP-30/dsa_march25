'''
Given an array of a interger, the objectice is to minimize the total cost of emptying the array. The cost
of removing an element is definied as the sum of all remaining elements in the array at the
time of removal.
'''

a = [3,5,1,-3]

def solve1(a):
    a = sorted(a)
    cost = 0
    summ = sum(a)
    for i in range(len(a)-1,-1,-1):
        cost += summ
        summ -= a[i]
    print(cost)

def solve(a):
    a = sorted(a,reverse=True)

    cost = 0
    for i in range(len(a)):
        cost += (i+1) * a[i]
    print(cost)

print(solve(a))