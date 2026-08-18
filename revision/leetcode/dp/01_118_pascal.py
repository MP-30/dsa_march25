
        

def generate(numRows):
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
    if numRows >0:
        result.append(start1)
    if numRows >1:
        result.append(start2)
    if numRows>2:
        for i in range(2,numRows):
            result.append(convert(result[-1]))
    return(result)
    
print(generate(5))    



    
# print(convert([1,4,6,4,1]))
            