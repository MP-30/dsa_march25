'''
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
s = ["h","e","l","l","o"]
def reverse_string(s):
    for i in range(0,len(s)//2):
        s[i],s[-(i+1)] = s[-(i+1)], s[i]
    print(s)
        
reverse_string(s)