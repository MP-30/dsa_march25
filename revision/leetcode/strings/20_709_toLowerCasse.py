s = "Hello"

class Solution:
    def toLowerCase(self, s: str) -> str:
        dictt = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z','A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
        result = []
        for i in s:
            if i in dictt.keys():
                result.append(dictt[i])
            else: result.append(i)
        return (''.join(result))
            
a = Solution()
print(a.toLowerCase(s))

