import math
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return math.ceil(4 * math.pi * (A**3))/3
    
s = Solution()
print(s.solve(4))