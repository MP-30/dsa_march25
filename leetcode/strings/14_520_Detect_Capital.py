'''
Example 1:
Input: word = "USA"
Output: true
Example 2:
Input: word = "FlaG"
Output: false
'''
word = "FlaG"
def check(word):
    condition_1 = word.upper()
    condition_2 = word.capitalize()
    condition_3 = word.lower()
    if word == condition_1 or word == condition_2 or word == condition_3:
        return True
    else:
        return False
    
print(check(word))