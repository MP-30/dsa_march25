s1 = '42'
s2 = ' -42'
s3 = "1337c)d3"
s4 = "0-1"
s5 = 'words and 987'
def myAtoi(s):
    ...
    sign = 1
    result = []
    a= 0
    for i in range(0,len(s)):
        if s[i] == ' ':
            continue
        elif s[i] =='-' :
            sign = -1
            a = i+1
            break
        elif s[i] == '+':
            sign = 1
            a = i+1
            break
        else:
            a= i    
            break
        
    for i in range(a,len(s)):
        if s[i].isalpha():
            break
        elif not s[i].isdigit():
            break
        elif s[i].isdigit():
            result.append(s[i])

    if len(result) == 0:
        return (int(0))
    else:
        num = (sign * int(''.join(result)))
        
    int_min, int_max = -2**31, 2**31-1
    
    if num < int_min:
        return int_min
    elif num > int_max:
        return int_max
    else: return num
    
            
print(myAtoi(s5))