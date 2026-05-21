A = "ABCGAG"
def solve(A):
    count_a = 0
    count_g = 0

    for i in A:
        if i == 'A':
            count_a +=1
        if i == 'G':
            count_g += count_a
    return count_g

print(solve(A))