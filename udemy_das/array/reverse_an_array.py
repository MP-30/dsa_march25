arr = [12,6,2,1,9,10,3]

length = len(arr)//2

for i in range(1,length+1):
    arr [i-1] , arr [-i] = arr [-i], arr [i-1]

print(arr)