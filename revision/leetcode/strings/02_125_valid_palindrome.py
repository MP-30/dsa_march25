'''
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
s = "0P"
def valid(s):
    new_str = s.lower()
    validate_str = []
    for i in new_str:
        if i.isalnum():
            validate_str.append(i)
    if validate_str == validate_str[::-1]:
        return True
    else: return False  
print(valid(s))