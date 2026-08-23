A = "110000111001"

def solve(A):
    csum = 0
    maxsum = 0

    start = 0
    best_start = 0
    best_end = 0

    for i in range(len(A)):
        if A[i] == '1':
            csum -= 1
        else:
            csum += 1

        if csum > maxsum:
            maxsum = csum
            best_start = start
            best_end = i

        if csum < 0:
            csum = 0
            start = i + 1

    if maxsum == 0:
        return []

    return [best_start + 1, best_end + 1]


print(solve(A))