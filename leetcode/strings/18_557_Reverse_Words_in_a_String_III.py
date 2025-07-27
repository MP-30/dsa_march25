s = "Mr Ding"

def reverse(s):
    start = 0
    new_list = []
    for i in range(0,len(s)):
        if s[i] == ' ' :
            new_list.append(s[start:i])
            start = i+1
        elif i == len(s)-1:
            new_list.append(s[start:i+1])
    for j in range(0,len(new_list)):
        new_list[j] = new_list[j][::-1]
    return(' '.join(new_list))
    
print(reverse(s))