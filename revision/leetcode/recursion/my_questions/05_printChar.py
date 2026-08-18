### 5. Print characters of a string one by one

# "abc" → a b c

def one(a : str, i=0):
    if i == len(a):
        return 
    print(a[i], end=' ')
    one (a, i+1)
    
one('ert')