def solve(A):
    left_prefix = [A[0]]
    right_prefix = [A[-1]]
    for i in range(1,len(A)):
        left_prefix.append(left_prefix[-1]+A[i])
    for j in range(len(A)-2,-1,-1):
        right_prefix.append(right_prefix[-1]+A[j])
    
    for k in range(0,len(A)):
        if(left_prefix[k] ==  right_prefix[(len(A)-1) - k]):
            return k
    else:
        return -1

# A = [-7,1,5,2,-4,3,0]
A = [1,2,3]
print(solve(A))