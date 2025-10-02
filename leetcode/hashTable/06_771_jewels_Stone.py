def numJewelsInStones(jewels, stones):
    a = list(jewels)
    count = 0
    for i in stones:
        if i in a:
            count +=1
    return(count)
    
    
jewels = "z"
stones = "ZZ"

numJewelsInStones(jewels,stones)