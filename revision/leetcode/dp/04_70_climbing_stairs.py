def climb(n):
    fibo = [0,1,1,2]
    if n == 1:
        fibo = [0,1,1]
    elif n == 2:
        fibo = [0,1,1,2]
    else:
        for i in range(2,n):
            fibo.append(fibo[-1] + fibo[-2])
    return fibo[-1]

print(climb(7))

