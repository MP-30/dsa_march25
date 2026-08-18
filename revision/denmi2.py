def function():
    i = 0
    sum = 0
    while(i < 100):
        sum = sum + i
        sum = i + sum
        print(sum)
        i += 1
    print(sum)
    
function()