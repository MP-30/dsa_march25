s = "PPALLP"

def atten(s):
    abcnt = 0
    consu_l = 0
    for i in s:
        if i == 'A':
            abcnt +=1
            if abcnt >1:
                return False
            consu_l = 0
        elif i == 'P':
            consu_l = 0
        elif i == 'L':
            consu_l +=1
            if consu_l >=3:
                return False
    else: return True    

print(atten(s))