### 3. Sum of first N numbers

# ```
# 1 + 2 + 3 + ... + N
# ```

def one(N):
    if N == 0:
        return 0
    ans = N + one(N-1)
    return ans

print(one(4))
    