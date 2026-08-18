'''
Example 1:
Input: a = "aba", b = "cdc"
Output: 3

Example 2:
Input: a = "aaa", b = "bbb"
Output: 3

Example 3:
Input: a = "aaa", b = "aaa"
Output: -1
'''
a = "aaa"
b = "aaa"
def longest(a,b):
    count = 0
    for i in range(0,len(a)):
        if a[i] != b[i]:
            count +=1
    if count>0:
        return count
    else: return -1
    
print(longest(a,b))