def chhh(text):
    '''
    b = 1, a = 1, l = 2, o = 2, n = 1, s = 1
    '''
    from collections import Counter
    dictt = Counter(text)
    count = []
    print(dictt)
    for i in 'balloon':
        if i in dictt:
            if i =='l' or i =='o':
                count.append(dictt[i]//2)
            else:
                count.append(dictt[i])
        else:
            return 0
        
    return min(count)

text = 'loonbalxballpoon'

print(chhh(text))