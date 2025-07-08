'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true 
'''
ransomNote = "aa"
magazine = "aab"
def ransom(ransomNote, magazine):
    dictt = {}
    for i in range(0,len(ransomNote)):
        if ransomNote[i] not in dictt:
            dictt[ransomNote[i]] = 1
        elif ransomNote[i] in dictt:
            dictt[ransomNote[i]] +=1
    dictt2 = {}
    for i in range(0,len(magazine)):
        if magazine[i] not in dictt2:
            dictt2[magazine[i]] = 1
        elif magazine[i] in dictt2:
            dictt2[magazine[i]] +=1
    print(f"dictt is {dictt}")
    print(f"dictt2 is {dictt2}")
    for a,b in dictt.items():
        print(f"checking for {a} for value {b} and expected is {dictt2[a]}")
        if a not in dictt2.keys():
            return False
        elif a in dictt2.keys():
            if dictt2[a] < b:
                return False
    else: return True
        
    
print(ransom(ransomNote, magazine))