class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_dict = {}
        for i in range(0,len(order)):
            order_dict [order[i]] = i 
        print(order_dict)
        
        for j in range(0,len(words)-1):
            length = min (len(words[j]), len(words[j+1]) )
            for k in range(length):
                if order_dict[words[j][k]] == order_dict[words[j+1][k]]:
                    continue
                
                elif order_dict[words[j][k]] < order_dict[words[j+1][k]]:
                    break
                
                elif order_dict[words[j][k]] > order_dict[words[j+1][k]]:
                    return False
                
            if len(words[j]) > len(words[j+1]):
                return False
                    
        return True
        
        
        
        
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

# words = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"

# words = ["apple","app"]
# order = "abcdefghijklmnopqrstuvwxyz"

ss  = Solution()
print(ss.isAlienSorted(words, order))