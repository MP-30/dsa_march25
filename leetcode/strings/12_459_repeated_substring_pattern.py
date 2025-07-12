s = "abcabcabcabcabcabc"
def repeated(s):
    subString = []
    initilizer = s[0]
    subString.append(initilizer)
    for i in range(0,len(s)):
        if s[(i+1):(i + len(subString))] != (''.join(subString)):
            subString.append(s[i])
    print(subString)
    
repeated(s)