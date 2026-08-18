'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
s = "leetcode"
def reverse_vowel(s):
    a = ['a','e','i','o','u','A','E','I','O','U']
    dictt = {}
    for i in range(0,len(s)):
        if s[i] in a:
            dictt[i] = s[i]
    print( dictt)
    original_keys = list(dictt.keys())
    reverse_value = list(dictt.values())
    reverse_value.reverse()
    new_dictt = dict(zip(original_keys, reverse_value))
    print(new_dictt)
    s_list = list(s)
    for j,k in new_dictt.items():
        s_list[j] = k
    return(''.join(s_list))
print(reverse_vowel(s))
