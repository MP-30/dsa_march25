# s = "paper"
# t = "title"
# s = "foo"
# t = "bar"
s = "badc"
t = "baba"
def isomorphic(s,t):
    dictt = {}
    if len(s) == len(t):
        for i in range(0,len(t)):
            dictt[s[i]] = t[i]
    
    print(dictt)
    print()
    if len(set(dictt.values())) != len(dictt.values()):
        print('------------')
        return False
    new_list = list(s)
    for j in range(0,len(new_list)):
        new_list[j] = dictt[new_list[j]]
    new_s =(''.join(new_list))
    if new_s == t:
        print(True)
    else: print(False)
    print(new_list)
    print(new_s)
    
print(isomorphic(s,t))