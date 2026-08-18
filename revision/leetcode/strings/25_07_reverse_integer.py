def reverse(x):
    ...
    min_range = -1 * 2**31
    max_range = 2**31 -1
    def convert(x):
        new_num = 0
        while x >0:
            new_num = new_num *10 + (x%10)
            x = x //10
        return int(new_num)
    if x ==0:
        c =  0
    elif x >0:
        c = convert(x)
        
    elif x <0:
        x = -1*x
        c =convert(x) * -1
    
    if c > max_range or c < min_range:
        return 0
    else: return c

# print(reverse(123))

n = 4
l = [i for i in range(1,n+1) if i % 2 == 0 ]
print(l)

