s1 = "listen"
s2 = "sileent"
def anagram(str1, str2):
    return(sorted(s1) == sorted(s2))

if __name__ == '__main__':
    print(anagram(s1,s2))