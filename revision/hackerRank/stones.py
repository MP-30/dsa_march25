# n = 4
# a = 10
# b = 100

n = 5
a = 2
b = 5

# def stones(n, a, b):
#     # s1 = 0
#     # s2 = [a,b]
#     # s3 = [s2[0]+s2[0],s2[0]+s2[1],s2[1]+s2[0],s2[1]+s2[1]]
#     # s4 = [s3[0]+s2[0], s3[0]+s2[1], s3[1]+s2[0], s3[1]+s2[1], s3[2]+s2[0], s3[2]+s2[1], s3[3]+s2[0], s3[3]+s2[1]]

#     start_value = min(a,b) * (n-1)
#     diff = abs(a-b)
#     rst = [start_value]
#     for i in range(n-1):
#         rst.append(rst[i]+diff)

#     print(rst)

# stones(n, a, b)

def stones(n,a,b):
    possible_values = set()  # Use a set to avoid duplicates
    for i in range(n):
        possible_values.add(a * (n - 1 - i) + b * i)
    return sorted(list(possible_values))


print(stones(n,a,b))