class Solution:
    def gcd(self,A,B):
        while B:
            A,B = B,A%B
        return A
    
A = int(input())
B = int(input())
    
s = Solution()
print(s.gcd(A,B))