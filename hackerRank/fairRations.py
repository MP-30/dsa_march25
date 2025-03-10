B = [2,3,4,5,6]

def fairRations(B):
    loaves = 0
    for i in range(0,len(B)-1):
        if B[i] %2 != 0:
            B[i] = B[i] + 1
            B[i+1] +=1
            loaves =+2
    if B[-1] %2 !=0:
        return ('No')
    return loaves
    

print(fairRations(B))