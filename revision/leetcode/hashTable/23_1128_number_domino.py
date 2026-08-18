from collections import defaultdict

def nnun(dominoes):
    dictt = defaultdict(int)
    
    for i in dominoes:
        dictt[(min(i), max(i))] += 1    
    
    count = 0
    
    for i in dictt.values():
        count += (i*(i-1))//2
    
    return count
    
    
dominoes = [[1,2],[2,1],[3,4],[5,6]]

# dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]

print(nnun(dominoes))


