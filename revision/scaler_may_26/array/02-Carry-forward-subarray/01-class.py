'''
Given a string s of lower case characters, return the count of pairs(i,j)
such that i < j and s[i] = 'a' and s[i] = 'g'
'''

s = ['b','a','a','g','d','c','a','g']
def solve(s):
    count = 0
    count_a = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count_a +=1
        if s[i] == 'g':
            count += (count_a)
    return  count
print((solve(s)))