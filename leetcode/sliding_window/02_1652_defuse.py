def sovle(code,k):
    length = len(code)
    if k == 0:
        return [0] * length
    result = [0] * length
    extended = code * 2
    
    if k > 0:
        window_sum = sum(extended[1:k+1])
        for i in range(length):
            result[i] = window_sum
            window_sum += extended[i+k+1] - extended[i+1]
    else:
        k = -k
        window_sum = sum(extended[length-k:length])
        for i in range(length):
            result[i] = window_sum
            window_sum += extended[length +i] - extended[length + i -k]
    
    return result
    
        
# code = [5,7,1,4]
# k= 3
# code1 = [1,2,3,4]
# k = 0
code = [2,4,9,3]
k = -2

print(sovle(code,k))