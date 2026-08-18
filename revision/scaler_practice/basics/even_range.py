def solve(A,B):
    prefix_even = [0]
    for i in range(len(A)):
        if A[i] % 2 ==0:
            prefix_even.append(prefix_even[i]+1)
        else:
            prefix_even.append(prefix_even[i]+0)
    result = []
    for l,r in B:
        result.append(prefix_even[r+1]-prefix_even[l])
    print(result)
    
    
    
A = [1,2,3,4,5]
B = [[0,2],[2,4],[1,4]]
print(solve(A,B))
s = [0,1,1,2,2,3]