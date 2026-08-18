### 2. Print numbers from N to 1

# Print in reverse: `N N-1 ... 1`.


def two(n):
    if n ==0: 
        return 
    print (n)
    two(n-1)