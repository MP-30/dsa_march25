def isPathCrossing(path):
    lt = [[0,0]]
    for i in path:
        if i == 'N':
            x = lt[-1][0] +1
            y = lt[-1][1] 
            new = [x,y]
            if new in lt:
                return True
            lt.append(new)
        elif i == 'S':
            x = lt[-1][0] -1
            y = lt[-1][1] 
            new = [x,y]
            if new in lt:
                return True
            lt.append(new)
        elif i == 'E':
            x = lt[-1][0]
            y = lt[-1][1] +1 
            new = [x,y]
            if new in lt:
                return True
            lt.append(new)
        elif i == 'W':
            x = lt[-1][0] 
            y = lt[-1][1] -1
            new = [x,y]
            if new in lt:
                return True
            lt.append(new)
    return False

    
path = 'NES'
print(isPathCrossing(path))