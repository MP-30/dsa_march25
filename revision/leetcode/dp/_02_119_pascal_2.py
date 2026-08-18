
def generate(rowIndex):
    rowIndex +=1
    def convert(l):
        dictt = {}
        for i in range(1,len(l)):
            dictt[i] = l[i] + l[i-1]
        new_l =[l[0],l[-1]]
        for j,k in dictt.items():
            new_l.insert(j,k)
        return(new_l)
    start1 = [1]
    start2 = [1,1]
    result = []
    
    if rowIndex >0:
        result.append(start1)
    if rowIndex >1:
        result.append(start2)
    if rowIndex>2:
        for i in range(2,rowIndex):
            result.append(convert(result[-1]))
    return(result[-1])
    
print(generate(3))

