### 7. Sum of digits of a number


# input 432 → output 4+3+2 = 9

def ss(a):
    if a == 0:
        return 0
    
    ans = a % 10 + ss(a//10)
    return ans

print(ss(432))