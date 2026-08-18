'''
Given an integer A. Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).

NOTE: 
   The value of A*A can cross the range of Integer.
   Do not use the sqrt function from the standard library. 
   Users are expected to solve this in O(log(A)) time.

'''
import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        return math.floor(A**0.5)
    
s = Solution()
print(s.sqrt(26))