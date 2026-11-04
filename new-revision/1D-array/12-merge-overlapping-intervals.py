'''
given a sorted list of overlapping intervals sorted based on the start time.
Merge of overlapping intervals and return the sorted list.
'''
N = 7
lst = [(0,2), (1,4),(5,6),(6,8),(7,10),(8,9), (12,14)]
def solve(lst):
    if not lst: return []
    a = list(lst[0])
    result = []
    for i in range(1,len(lst)):
        if lst[i][0] <= a[1]:
            a[1] = max(lst[i][1], a[1])
        elif lst[i][0] > a[1]:
            result.append(a)
            a = list(lst[i])
    result.append(a)
    return result

print(solve(lst))