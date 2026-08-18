emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output = 2
Explanation= "testemail@leetcode.com" and "testemail@lee.tcode.com" 


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        sett = set()
        for i in emails:
             a = i.split('@')
             a1 = a[0].replace('.','')
             a1 = a1.split('+')
             sett.add(f"{a1[0]}@{a[1]}")
        return (len(sett))
             
             
re = Solution()
print(re.numUniqueEmails(emails))
         
         
