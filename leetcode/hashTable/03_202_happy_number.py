def isHappy(n):
    summ = 0
    table = {}
    while True:
        while n >0:
            a = n%10
            n = n//10
            summ+=(a**2)
        if summ in  table:
            return False
        elif summ not in table.keys():
            table[summ] = 1
        if summ == 1:
            return True
        else:
            n = summ
            summ = 0
    
print(isHappy(2))