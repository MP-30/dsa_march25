def chuchu(arr):
    dictt = {}
    a = sorted(arr)
    rank = 1
    for i in range(0,len(a)):
        if a[i] not in dictt:
            dictt[a[i]] = rank
            rank +=1
    for j in range(len(arr)):
        arr[j] = dictt[arr[j]]
    print(dictt)
    return(arr)        
    
arr = [37,12,28,9,100,56,80,5,12]

print(chuchu(arr))