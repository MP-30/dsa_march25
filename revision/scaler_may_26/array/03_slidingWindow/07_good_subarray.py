A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
output = 65
def solve(A,B):
    result = 0
    for i in range(len(A)):
        summ = 0
        for j in range(i,len(A)):
            length = j - i +1
            new_sum = summ + A[j]
            summ = new_sum

            if length % 2 == 0 and summ < B:
                result +=1
            elif length %2 !=0 and summ > B:
                result +=1
    return result
print(solve(A,B))
