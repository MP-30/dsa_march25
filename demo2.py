# data
nested = [[1, 2], [3, 4], [5, 6]]

# excep
a = [1, 2, 3, 4, 5, 6]

def to_check(nested):
    result = []
    for i in nested:
        for j in i:
            result.append(j)
    print(result)
    
to_check(nested)