s = "{[()]}"
def isValid(s):
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != bracket_map[ch]:
                return False
            stack.pop()
    return len(stack) == 0
print(isValid(s))