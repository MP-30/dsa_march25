def solve(s):
    count = 0
    i = 0
    j = 2
    while j < len(s):
        if len(s[i:j+1]) == len(set(s[i:j+1])):
            count +=1
        i +=1
        j +=1
    return count
s = "aababcabc"
print(solve(s))