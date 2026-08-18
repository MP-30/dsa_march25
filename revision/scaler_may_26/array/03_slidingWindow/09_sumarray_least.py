A = [3, 7, 90, 20, 10, 50, 40]
B = 3
output = 3

def solve(A,B):
    result = 0
    i = 0
    j = B
    average = sum(A[:B])
    least = average

    while j < len(A):
        average = average - A[i] + A[j]
        local_result = (average)

        if local_result < least:
            least = local_result
            result = i +1
        i +=1
        j +=1
    return result


print(solve(A,B))