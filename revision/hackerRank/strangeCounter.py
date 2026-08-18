# approach 1
'''
t = 6
q = 8
def strangeCounter(t):
    lst = [3]
    timer = [0]
    # lst.append(3)
    q = 12
    while lst[-1] <=q:
        l = lst[-1]*2
        lst.append(l)
    print(f'list is {lst}') 
    for i in lst:
        # print(f' this is {i}')
        for j in range(i,0,-1):
            timer.append(j)
    # print(f'timer is {timer}')
    # print(f'value on a perticular t is {timer[6]}')
    return(timer[t])

strangeCounter(t)
'''
t = 9
def strangeCounter(t):
    start_time = 1
    cycle_start_value = 3
    while (start_time + cycle_start_value -1) < t:
        start_time += cycle_start_value
        cycle_start_value *=2
    answer = cycle_start_value - abs(start_time - t)
    return(answer)

print(strangeCounter(t))