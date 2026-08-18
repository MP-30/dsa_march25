sentence = "I speak Goat Latin"
sentt = "The quick brown fox jumped over the lazy dog"

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        to_done = (sentence.split())
        solution = []
        vowel = ['a','e','i','o','u', 'A', 'E', 'I','O','U']
        for i,j in enumerate(to_done):
            if j[0] in vowel:
                solution.append(j + 'ma' + ((i+1)*'a'))
            else:
                solution.append(j[1:] +  j[0] + 'ma' +   ((i+1)*'a'))
        return(' '.join(solution))