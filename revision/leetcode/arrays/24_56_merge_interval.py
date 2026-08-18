intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]
intervals3 = [[4,7],[1,4]]
intervals4 = [[4,7],[1,7],[3,7],[7,9],[5,10],[2,8],[12,16]]

def merge(intervals):
    lt = [intervals[0]]
    for i in range(1,len(intervals)):
        inserted = False
        for j in range(0,len(lt)):
            if intervals[i][0] < lt[j][0]:
                inserted = True 
                lt.insert(j,intervals[i])
                break
        if not inserted:
            lt.append(intervals[i])
    
    i = 0
    while i < len(lt) -1:
        if lt[i][1] >= lt[i+1][0]:
            merged = [lt[i][0], max(lt[i][1], lt[i+1][1])]
            del lt[i: i +2]
            lt.insert(i, merged)
        else:
            i +=1
    
    return(lt)
               
        
    
print(merge(intervals4))

'''
check this way also

start with [1,3]
compare with [2,6] → merge → [1,6]
compare with [8,10] → no merge → [1,6],[8,10]
compare with [9,11] → merge → [1,6],[8,11]
compare with [15,18] → no merge → [1,6],[8,11],[15,18]

'''