'''
Given an array of integers A and an integer B, find and return the minimum number of swaps required
to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.
'''
# A = [1, 12, 10, 3, 14, 10, 5]
# B = 8
# A = [5, 17, 100, 11]
# B = 20
A = [52,7,93,47,68,26,51,44,5,41,88,19,78,38,17,13,24,74,92,5,84,27,48,49,37,59,3,56,79,26,55,60,16,83,63,40,55,9,96,29,7,22,27,74,78,38,11,65,29,52,36,21,94,46,52,47,87,33,87,70]
B = 19
def solve(A,B):
    window_size = 0
    for i in A:
        if i <= B:
            window_size +=1
    if window_size <= 1:
        return 0
    j = 0
    k = window_size
    current_bad = 0
    for m in range(j,k):
        if A[m] > B:
            current_bad +=1
    min_swap = current_bad
    while k < len(A):
        if A[k] > B:
            current_bad +=1
        if A[j] > B:
            current_bad -=1

        min_swap = min(min_swap, current_bad)
        j += 1
        k += 1
    return min_swap

def solve1(A,B):
    window_size = 0
    for i in A:
        if i <= B:
            window_size +=1
    j = 0
    k = j + window_size
    min_swap = float('inf')
    while k <= len(A):
        local = 0
        for l in range(j, k):
            if A[l] > B:
                local +=1
        min_swap = min(min_swap, local)
        j +=1
        k +=1

    return min_swap

print(solve(A,B))