def merge(word1, word2):
    result = []
    len_1 = len(word1)
    len_2 = len(word2)
    i = 0
    j = 0
    for _ in range(max(len_1, len_2)):
        if i < len_1:
            result.append(word1[i])
        if j < len_2:
            result.append(word2[j])
        i +=1
        j +=1
    return (''.join(result))
    ...
    
word1 = 'ab'
word2 = 'pqrs'
print(merge(word1,word2))