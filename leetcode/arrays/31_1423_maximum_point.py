def maxScore(a: list[int], b: int) -> int:
    prefix = [a[0]]
    subfix = [a[-1]]
    for i in range(1,len(a)):
        prefix.append(prefix[-1] + a[i])
    for j in range(len(a)-2,-1,-1):
        subfix.append(subfix[-1] + a[j])
    result = prefix[b-1]
    result1 = subfix[b-1]
    for i in range(0,b-1):
        if prefix[b-2-i] + subfix[i] > result:
            result = prefix[b-2-i] + subfix[i]
    if result > result1:
        return result
    else: return result1