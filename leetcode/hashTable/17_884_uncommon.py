def uncommonFromSentences1(s1, s2):
    dict_s1 = {}
    dict_s2 = {}
    s1 = s1.split(' ')
    s2 = s2.split(' ')
    for i in s1:
        if i not in s2:
            if i not in dict_s1:
                dict_s1[i] =1
            elif i in dict_s1:
                dict_s1[i] +=1
    for i in s2:
        if i not in s1:
            if i not in dict_s2:
                dict_s2[i] =1
            elif i in dict_s2:
                dict_s2[i] +=1
    results = []
    
    for i, j in dict_s1.items():
        if j ==1:
            results.append(i)

    for i , j in dict_s2.items():
        if j ==1:
            results.append(i)
    print(results)

# s1 = 'this apple is sweet'
# s2 = 'this apple is sour'

# s1 = 'apple apple'
# s2 = 'banana'

from collections import Counter
def uncommonFromSentences(s1, s2):
    words = s1.split() + s2.split()
    count = Counter(words)
    
    return [word for word, freq in count.items() if freq ==1]


s1 = 's z z z s'
s2 = 's z ejt'
print(uncommonFromSentences(s1,s2))