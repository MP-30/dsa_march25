flowerbed = [1,0,0,0,0,0,1]
n =3

def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] ==0:
            left = (i ==0) or (flowerbed[i-1] ==0)
            right = (i == len(flowerbed)-1) or (flowerbed[i+1] ==0)
            
            if left and right:
                flowerbed[i] =1
                count +=1
        if count >=n:
            return True
    return False
    # print(flowerbed)
        
            
        
        
        
print(canPlaceFlowers(flowerbed,n))