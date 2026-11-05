list_1 = [(1,2),(3,5),(7,9)]
list_2 = [(2,5), (5,6)]

def sorted_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i][0] < list_2[j][0]:
            result.append(list_1[i])
            i +=1
        else:
            result.append(list_2[j])
            j +=1
    while i < len(list_1):
        result.append(list_1[i])
        i +=1
    while j < len(list_2):
        result.append(list_2[j])
        j +=1
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