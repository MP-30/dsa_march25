def solve(mat):
    result = []
    for i in range(len(mat)):
        unique = []
        for j in range(len(mat[0])):
            local_unique_bottom = set()
            local_unique_top = set()
            k = i +1
            l = j+1
            while k < len(mat) and l < len(mat[0]):
                local_unique_bottom.add(mat[k][l])
                k +=1
                l +=1
            a = i -1
            b = j -1
            while a >= 0 and b >=0 :
                local_unique_top.add(mat[a][b])
                a -=1
                b -=1
            unique.append(abs(len(local_unique_top)-len(local_unique_bottom)))
            local_unique_bottom = []
            local_unique_top = []
                
        result.append(unique)
    return result
    ...
    
mat = [
        [1,2,3],
        [3,1,5],
        [3,2,1]]

print(solve(mat))