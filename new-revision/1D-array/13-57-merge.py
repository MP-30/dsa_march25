list_1 = [(1,2),(3,5),(7,9)]
list_2 = [5,6]

def sorted_list(list_1, list_2):
    result = []
    for i in range(0,len(list_1)):
        if list_2[0] < list_1[i][0]:
            result.append(list_2)
            result.extend(list_1[i:])
            return result
        else:
            result.append(list_1[i])
    result.append(list_2)
    return result

def solve(list_1, list_2):

    base = sorted_list(list_1,list_2)
    if not base: return []
    a = list(base[0])
    result = []
    for i in range(1,len(base)):
        if base[i][0] <= a[1]:
            a[1] = max(base[i][1], a[1])
        elif base[i][0] > a[1]:
            result.append(a)
            a = list(base[i])
    result.append(a)
    return result

print(solve(list_1, list_2))