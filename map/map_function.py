def myfunc(n,m):
    return (n+m)

list1 = [1,2,3,4,5,10]
list2 = [4,5,6,7,8]
x = (map(myfunc, list1, list2 ))
print(x)
print(list(x))