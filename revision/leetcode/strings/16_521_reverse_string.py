s= "123456789"
k = 3
def reserse(s,k):
    chunck = []
    chunck2 = []
    for i in range(0,len(s),k):
        chunck.append(s[i: i+k])
    for j in range(0,len(chunck)):
        if j %2 == 0:
            chunck2.append((chunck[j])[::-1])
        else: chunck2.append(chunck[j])
    return(''.join(chunck2))
print(reserse(s,k))
