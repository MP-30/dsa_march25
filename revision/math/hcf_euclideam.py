num1 = 24
num2 = 54

def calculate(x,y):
    while(y):
        x, y = y , x % y
    return x
print(calculate(num1, num2))