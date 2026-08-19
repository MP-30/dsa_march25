# s = "adaa"
# chars = "d"
# vals = [-1000]
# output = 2

# s = "abc"
# chars = "abc"
# vals = [-1,-1,-1]
# Output= 0

s = "zox"
chars = "zoxr"
vals = [2,-5,-4,-5]
output = 2


def solve(s,chars, vals):
    check = {}
    result = []
    for j in range(len(chars)):
        check[chars[j]] = vals[j]
    for i in range(len(s)):
        if s[i] in check.keys():
            result.append(check[s[i]])
        else:
            result.append(ord(s[i]) -96)
    final = max(0,result[0])
    for k in range(1,len(result)):
        if result[k-1] + result[k] > result[k]:
            result[k] += result[k - 1]
        final = max(final,result[k])

    print(check)
    print(result)
    return (final)

print(solve(s,chars, vals))