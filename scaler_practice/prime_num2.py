class Solution:
    # @param A : list of integers
    # @return an integer
   
    def solve(self, A):
        count = 0
        for i in A:
            if i ==2:
                count +=1
            elif i >2:
                for j in range(2,(i//2)+1):
                    if i % j == 0:
                        break
                    else: count +=1
        return count
A = list(map(int, input().split()))
# s = Solution()
# print(s.solve(A))
for i in A:
    print(type(i))