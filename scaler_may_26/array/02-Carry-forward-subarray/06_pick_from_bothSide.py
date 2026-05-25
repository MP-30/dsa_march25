A = [ 2, 3, -1, 4, 2, 1 ]
B = 4
output = 9

def solve(A,B):
    fwd_prefix = [0]
    bkw_prefix = [0]
    for i in range(B):
        fwd_prefix.append(fwd_prefix[-1] + A[i])
    # print(fwd_prefix)
    for j in range(len(A)-1,len(A)-1-B,-1):
        bkw_prefix.append(bkw_prefix[-1]+A[j])
    # print(bkw_prefix)
    result = fwd_prefix[B]
    for k in range(0,B+1):
        result = max((fwd_prefix[(B)-k]+ bkw_prefix[k]), result)
    return(result)
print(solve(A,B))
