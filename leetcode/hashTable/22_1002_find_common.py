words = ["bella","label","roller"]

# words = ['cool', 'lock', 'cook']

def huhu(words):
    from collections import Counter
    result = (Counter(words[0]))
    
    for i in range(1,len(words)):
        a = Counter(words[i])
        new_result = {}
        for j,k in a.items():
            if j in result:
                new_result[j] = min(k, result[j])
        result = new_result
        
    final_result = []
    for i,j in result.items():
        for _ in range(j):
            final_result.append(i)
    return final_result
    
    

print(huhu(words))