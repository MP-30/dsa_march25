'''
The product of two number is equal to the product of the least common multiple and greatest common divisor of those two number.
Number1 * Number2 = LCM * GCD
'''
num1 = 54
num2 = 24

def compute_gcd(x,y):
    while(y):
        x,y = y, x%y
    return x

def compute_lcm(x,y):
    lcm = (x*y)//compute_gcd(x,y)
    return lcm
print(compute_lcm(num1, num2))