title = "First leTTer of EACH Word"

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        result0 = title.split()
        for i in result0:
            if len(i)<=2:
                result.append(i.lower())
            else: result.append(i.capitalize())
        return (' '.join(result))
    
s = Solution()
print(s.capitalizeTitle(title))