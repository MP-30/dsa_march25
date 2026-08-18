s = "a"
def length(s):
    count = 0
    i = -1

    while abs(i) <= len(s) and s[i] == ' ':
        i -= 1

    while abs(i) <= len(s) and s[i] != ' ':
        count += 1
        i -= 1
    return count
print(length(s))
# print(s[-5:-1])