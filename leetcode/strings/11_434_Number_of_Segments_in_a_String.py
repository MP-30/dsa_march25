'''
Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:
Input: s = "Hello"
Output: 1
'''
s = "Hello"
def continues(s):
    base_count = 0
    if len(s)>0:
        if ' ' not in s:
            return (base_count +1)
        if s[0] != ' ':
            base_count +=1
        for i in range(1,len(s)):
            if s[i] != ' ' and s[i-1] == ' ':
                base_count +=1
        return base_count
    else:
        return base_count
    
print(continues(s))