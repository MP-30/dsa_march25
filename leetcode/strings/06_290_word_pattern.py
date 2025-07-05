pattern = "abba"
s = "dog cat cat fish"

def patterns(pattern, s):
    s1 = s.split(' ')
    dictt = {}
    if len(s1) != len(pattern):
        return False
    for i in range(0,len(pattern)):
        if pattern[i] in dictt.keys():
            if dictt[pattern[i]] != s1[i]:
                return False
        
        dictt[pattern[i]] = s1[i]
    if len(dictt.values()) != len(set(dictt.values())):
        return False
    return True
    
print(patterns(pattern, s))