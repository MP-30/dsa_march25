'''
The highest common factor or greatest common divison of two number is the largest positive integer that perfectly divides the two given numbers.
'''

x = 24
y = 54
def compute_hcf(x,y):
    if x > y:
        smallest = y
    else: smallest = x
    for i in range(1,smallest+1):
        if (x % i == 0) and (y% i ==0):
            hcf = i
    return hcf
print(compute_hcf(x,y))