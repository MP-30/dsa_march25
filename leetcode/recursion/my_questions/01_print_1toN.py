### 1. Print numbers from 1 to N

# Use recursion to print `1 2 3 ... N`.

def one(n):
    if n ==0: 
        return 
    one(n-1)
    print (n)
    
    
one(9)