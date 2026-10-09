def isValid(s: str) -> bool:
    # A string with an odd length can never be balanced
    if len(s) % 2:
        return False

    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in bracket_map:
            # Closing bracket: it must match the most recent unclosed opener
            if not stack or stack[-1] != bracket_map[ch]:
                return False
            stack.pop()
        # Any other character is ignored

    # Every opener must have been closed
    return not stack


# Tests
tests = {
    "{[()]}": True,
    "{{]{})()": False,
    "()": True,
    "()[]{}": True,
    "(]": False,
    "([)]": False,
    "((": False,
    ")(": False,
    "": True,
    "a(b)c": True,
}

for s, expected in tests.items():
    result = isValid(s)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: isValid({s!r}) = {result}")