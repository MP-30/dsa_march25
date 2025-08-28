'''
You are given a character string A having length N.

The string consists of 2 types of characters:

Alphabets : ['a'-'z', 'A'-'Z']
Digits: ['0'-'9']
You have to tell the count of characters of the maximum occuring character type.
'''

class Solution:
    # @param A : string
    # @return an integer
    def helper_char(self,A):
        charr = []
        for i in range(ord('a'), ord('z')+1):
            charr.append(chr(i))
        for j in range(ord('A'), ord('Z')+1):
            charr.append(chr(j))        
        return (charr)
    
    def helper_digit(self,A):
        digtt = []
        for k in range(ord('0'), ord('9')+1):
            digtt.append(chr(k))
        return (digtt)
    
    def solve(self, A):
        charrr = self.helper_char(A)
        digitt = self.helper_digit(A)
        count_char = 0
        count_digit = 0
        for i in A:
            if i in charrr:
                count_char +=1
            elif i in digitt:
                count_digit +=1
        return max(count_digit, count_char)
                
                
        
A = "M1234"
s = Solution()
print(s.solve(A))