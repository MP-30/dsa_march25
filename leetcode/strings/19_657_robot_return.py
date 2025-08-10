moves = "DURDLDRRLL"


def robot(moves):
    listt = []
    for i in moves:
        if i == 'R':
            listt.append(-1)
        elif i == 'L':
            listt.append(1)
        elif i == 'U':
            listt.append(-2)
        elif i == 'D':
            listt.append(2)
    if sum (listt) == 0:
        return True
    else: return False
print(robot(moves))