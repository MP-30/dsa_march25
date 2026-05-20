from os import PRIO_PGRP

A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
output = [10,5]

def range_sum(A,B):
    pre_sum = [0]
    for i in range(len(A)):
        pre_sum.append((A[i])+ pre_sum[-1])
    result = []
    for a,b in B:
        result.append(pre_sum[b+1] - pre_sum[a])
    return (result)
print(range_sum(A,B))