A = [2,1,6,4]
output = 1
B = [1,1,1]
outputA = 3

def solve(A, ):
    result = 0
    right_even_sum = 0
    right_odd_sum = 0
    for i in range(len(A)):
        if i % 2 == 0:
            right_even_sum += A[i]
        else:
            right_odd_sum += A[i]

    left_even_sum = 0
    left_odd_sum = 0

    for i in range(len(A)):
        if i % 2 == 0:
            right_even_sum -= A[i]
        else:
            right_odd_sum -= A[i]

        new_even = left_even_sum + right_odd_sum
        new_odd = left_odd_sum + right_even_sum

        if new_even == new_odd:
            result +=1

        if i % 2 == 0:
            left_even_sum += A[i]
        else:
            left_odd_sum += A[i]

    return  result

print((solve(A)))