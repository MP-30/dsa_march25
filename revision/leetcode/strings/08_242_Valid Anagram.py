'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
'''
s = "anagram"
t = "nagaram"
def validate(s,t):
    # dictt = {}
    # for i in range(0,len(s)):
    #     if s[i] not in dictt:
    #         dictt[s[i]] = 1
    #     elif s[i] in dictt:
    #         dictt[s[i]] +=1
    # return(dictt)
    s1 = sorted(s)
    t1 = sorted(t)
    if s1 == t1:
        return True 
    else: return False

print(validate(s,t))