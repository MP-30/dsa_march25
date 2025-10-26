# file = open("file_handling/hello.txt","r")
# if file:
#     print(file.read())
#     print(type(file))
# file.close()

# age = input('Enter your age: ')
# f = open("file_handling/age.txt",'w')
# f.write(age)
# f.close()
    
# f = None 
# for i in range (5): 
#     with open("data.txt", "w") as f: 
#         if i > 2: 
#             break 
# print(f.closed)

# with open("file_handling/age.txt","r") as f:

#     count = 0

#     data = f.readlines()

#     words = data.split()

#     for word in words:

#         count += 1

#     print(count)

# N = int(input())
# A = list(map(int, input().split()))
# X = int(input())
# Y = int(input())

# A.insert(X-1, Y)
# for i in A:
#     print(i, end=" ")


# A = 3
# B = 2
# C = [[4, 1], [1, 3], [6, 2]]

# def solve(A,B,C):
#     result = []
#     for j in range(B):
#         count = 0
#         for i in range(A):
#             count +=(C[i][j])
#         result.append(count)

#     print(result)
            
# print(solve(A,B,C))



import re

def findd(file_path):
    pattern = r"\d"  # match every digit (0–9)
    max_digits = -1
    max_line = ""   # store the line with most digits

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # count number of digits in current line
            digit_count = len(re.findall(pattern, line))
            
            # if this line has more digits than previous max, update
            if digit_count > max_digits:
                max_digits = digit_count
                max_line = line.rstrip("\n")  # remove trailing newline only

    return max_line
# /config/workspace/file.txt


def hhee(filepath):
    all = {}
    result = []
    with open(filepath, "r")as file:
        for line in file :
            line1 = line.rstrip('\n') 
          
            if line1 not in all:
                all[line1] = 1
            elif line1 in all:
                all[line1] +=1
    for i , j in all.items():
        if j > 1:
            result.append(i)
     
    return(result)
    

hhee('file_handling/hello.txt')
