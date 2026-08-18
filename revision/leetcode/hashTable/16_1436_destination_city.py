def destCity(paths):
    start_path = []
    end_path = []
    if len(paths) <2:
        return(paths[0][1])
    for i in paths:
        start_path.append(i[0])
        end_path.append(i[1])
    # print(start_path, end_path)
    
    start_path = set(start_path)
    end_path = set(end_path)
    for i in end_path:
        if i not in start_path:
            return i
    
    
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# paths = [["B","C"],["D","B"],["C","A"]]
# paths = [["A","Z"]]
print(destCity(paths))