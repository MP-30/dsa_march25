words = ["Hello","Alaska","Dad","Peace"]

def keyboard(words):
    str1 = "qwertyuiop"
    str2 = "asdfghjkl"
    str3 = "zxcvbnm"
    result = []
    for i in words:
        local1 = 0
        local2 = 0
        local3 = 0
        to_test = len((set(i.lower())))
        for j in (set(i.lower())):
            if j in str1:
                local1 +=1
            elif j in str2:
                local2 +=1
            elif j in str3:
                local3 +=1
        if local1 == to_test or local2 == to_test or local3 == to_test:
            result.append(i)
            local1 = 0
            local2 = 0
            local3 = 0
    return(result)
    
    
print(keyboard(words))