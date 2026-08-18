# A = [3,12,11,11,11,15]
# B = 12
A = [4, 1, 1]
B = 5

output = 4

def solve(A,B):
    prefix = [0]
    count = 0
    for i in range(len(A)):
        prefix.append(prefix[-1]+A[i])
    print(prefix)
    for j in range(1,len(prefix)):
        for k in range(j, len(prefix)):
            if prefix[k] < B:
                count +=1
            if prefix[k] >= B:
                break
        prefix = [x - prefix[j] for x in prefix]
    print(count)
print(solve(A,B))
#
# A = [3,12,11,11,11,15]
# [0, 3, 15, 26, 37, 48, 63]
# A = [2, 5, 6]
# B = 10


'''
start both left and right form 0. right will be use to add the values and left will use to remove the values
'''

