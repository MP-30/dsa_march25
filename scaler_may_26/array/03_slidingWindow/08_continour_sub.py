A = [1, 11, 2, 3, 15]
B = 10
output = 4

def solve(A,B):
    result = 0
    i = 0
    length = len(A)
    while i < length:
        j = i
        summ = 0
        while j < length:
            summ += A[j]
            if summ < B:
                result +=1
            elif summ >= B:
                break
            j +=1
        i +=1
    return  result

print(solve(A,B))