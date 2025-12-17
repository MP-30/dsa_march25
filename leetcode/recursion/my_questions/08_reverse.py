### 8. Reverse digits of a number

# Convert `432 → 234`.


def ss(a , i =0):
    if a == 0:
        return i
    
    i = 10 * i + (a %10)
    i = ss(a//10, i)
    return i

print(ss(432))