'''
approch one
n = 5
c = [0,4]

def flatlandSpaceStations(n,c):
    max_distance = 0
    my_list = []
    for i in range(0,n):
        my_list.clear()
        for j in c:
            my_list.append(abs(i-j))
        if (min(my_list) >= max_distance):
            max_distance = min(my_list)
        else:
            pass
    return(max_distance)

print(flatlandSpaceStations(n,c))
'''

# approch two
n = 10
c = [2,6]

def flatlandSpaceStations(n,c):
    c.sort()
    max_distance = 0

    # for start
    max_distance = max(max_distance, c[0])
    # for end
    max_distance = max(max_distance, ((n-1) - c[-1])) 
    # for mid
    for i in range(0,len(c)-1):
        dist = (c[i+1] - c [i])//2
        max_distance = max(max_distance, dist)

    return max_distance

print(flatlandSpaceStations(n,c))