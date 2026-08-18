def chuchu(s, goal):
    for _ in range(0,len(s)):
        s =  s[1:]+ s[:1]
        if s == goal:
            return True
    return False
        
    
    
    
s = 'abcde'
goal = 'abced'
print(chuchu(s, goal))