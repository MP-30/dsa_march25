b = 'AABBCC'

def happyLadybugs(b):
    bug_counts = {}
    
    for char in b:
        if char in bug_counts:
            bug_counts[char] += 1
        else:
            bug_counts[char] = 1

    if '_' not in bug_counts:
        for i in range(len(b)):
            print(i)
            if (i > 0 and b[i] == b[i - 1]) or (i < len(b) - 1 and b[i] == b[i + 1]):
                continue
            return 'NO'
        return 'YES'

    for char in bug_counts:
        if char != '_' and bug_counts[char] == 1:
            return 'NO'

    return 'YES'


    

print(happyLadybugs(b))

# dict = {1:2,2:3,3:4}
# print(len(dict))