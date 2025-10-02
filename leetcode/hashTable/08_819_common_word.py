def mostCommonWord(paragraph, banned):
    a = paragraph.replace(' ', ',')
    a = a.strip()
    a = list(a.split(','))
    new_lst = {}
    for i in a:
        new_word = ""
        for j in range(len(i)-1,-1,-1):
            if i[j].isalpha():
                new_word += i[j]
        new_word = (new_word[::-1]).lower()
        if new_word not in new_lst and new_word not in banned:
            new_lst[new_word] = 1
        elif new_word in new_lst and new_word not in banned:
            new_lst[new_word] +=1
    max = 0
    max_word = ''
    for j,k in new_lst.items():
        if k > max and j!='':
            max = k
            max_word = j
    return max_word
    
    
paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph2 = "a, a, a, a, b,b,b,c, c"
banned1 = ['hit']
banned2 = ["a"]


# a = paragraph2.replace(' ',',')
# a = a.strip()
# print(a)
a = ''
# print(a.isalpha())

print(mostCommonWord(paragraph2, banned2))