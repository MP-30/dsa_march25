def distance(s,c):
    result = []
    a = float('inf')
    for i in range(0,len(s)):
        if s[i] != c:
            a+=1
            result.append(a)
        elif s[i] ==c:
            a = 0
            result.append(a)
    
    a = float('inf')
    for j in range(len(s)-1,-1,-1):
        if s[j] != c:
            a +=1
            if result[j] > a:
                result[j] = a
        elif s[j] == c:
            a = 0
    return (result)
    
# s = "loveleetcode"
# c = "e"
s = 'aaab'
c = 'b'

print(distance(s,c))