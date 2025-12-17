### 4. Factorial of N

# n! = n × (n-1)!

def one (N):
    if N == 0:
        return 1
    
    ans = N * one(N-1)
    
    return ans

print(one(N=5))