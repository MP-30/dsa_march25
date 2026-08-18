s = "abcabcabcabcabcabc"
def repeated(s):
    for i in range(1, len(s) // 2 + 1):
        sub = s[:i]
        if len(s) % len(sub) != 0:
            continue

        result = True
        start_point = 0
        end_point = len(sub)

        while result and end_point <= len(s):
            if s[start_point:end_point] != sub:
                result = False
            start_point += len(sub)
            end_point += len(sub)

        if result:
            return True
    return False
 
    
print(repeated(s))