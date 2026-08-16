'''
find noble with duplicate
arr[i] is noble if count of elements smaller then arr[i] is equal to arr[i], where arr[i] is
element at index i
'''
a = [-10,1,1,3,100]
ans = 3
b = [-10,1,1,2,4,4,4,8,10]
def solve(f):
    f = sorted(f)
    ans = 0
    if f[0] == 0:
        ans +=1
    for i in range(1,len(f)):
        if f[i] != f[i-1]:
            less = i
        if f[i] == less:
            ans +=1

print(solve(b))