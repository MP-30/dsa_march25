strr = 'ABCDEFGHIJKLMNONQRSTUVWXYZ'

columnNumber = 701
def logic(n):
    listt = ''
    while n >0:
        n -=1
        rem = n % 26
        listt = chr(65 + rem) + listt
        n = n// 26
    print(listt)
    
logic(columnNumber)