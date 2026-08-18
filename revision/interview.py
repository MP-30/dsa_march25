# 1.  BALANCED parentheses
# ‘{ [ ( ( ) ) ] }’ balanced ->
# { [ ( ] ) } not balanced
# { } { ( ( ) { } [ ] )  } balanced
# { ( [ ) ] } not balanced
# INPUT : ‘{ ( [ ) ] }’
# OUTPUT : NOT BALANCED

a = "{ [ ( ( ) ) ] }"

dicttt = {'{':'}', '(':')', '[':']'}
# a.split()
def solve(a):
    # print(a.split("'"))
    b = []
    if len(a) == 0:
        return 'balanced'
    for i in a:
        if len(b) == 0:
            b.append(i)
        elif b[-1] != i:
            b.append(i)
        elif b[-1] == i:
            ...




solve(a)