def solve(s):
    prefix = [0]
    prefix_0 = [0]
    for i in s:
        prefix.append(prefix[-1]+ int(i))
        if i == '0':
            prefix_0.append(prefix_0[-1] + 1)
        else: prefix_0.append(prefix_0[-1]+0)

    max_sum = 0
    for i in range(1,len(s)):
        left = prefix_0[i]
        right = prefix[-1] - prefix[i]
        max_sum = max(max_sum, left+right)
    return max_sum
    
s = '1111'
print(solve(s))