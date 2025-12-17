### 6. Count digits of a number

# input 456 → output 3

def one(a: int):
    if a ==0:
        return 0
    
    return 1 + one(a// 10)
    
    
print(one(345))