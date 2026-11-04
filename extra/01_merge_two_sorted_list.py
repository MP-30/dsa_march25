a = [1,3,5,7]
b = [4,5,6,8,10]
def solve(a,b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b [j]:
            result.append(a[i])
            i +=1
        elif a[i] >= b[j]:
            result.append(b[j])
            j +=1
    while i < len(a):
        result.append(a[i])
        i+=1
    while j < len(b):
        result.append(b[j])
        j += 1

    return result


print(solve(a,b))