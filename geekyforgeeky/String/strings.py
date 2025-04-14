# Check if a string is palindrome or not

str3 = "madam"
str2 = "racecar"
str1 = "121"
str4 = "abba" 
str5 = "abab" 
str6 = "abcabc" 

def check_palidrome(a):
    for i in range(0,len(a)):
        if a[i] == a[-(i+1)]:
            pass
        else:
            return(False)
    return True



# Check whether the string is Symmetrical or Palindrome


def check_sys_pali(a):
    b = 0
    for i in range(0,len(a)):
        b = 1
        if a[i] == a[-(i+1)]:
            b = 1
        else:
            b = 2
    if b == 1:
        print('b=1')
        return ('String is palindrome')
    elif b == 2:
        str1_len = len(a)//2
        if len(a) % 2 == 0:
            print('b=2 even')
            if a[0:str1_len] == a[str1_len:len(a)]:
                b = 3
                return ('String is symmetrical')
        elif len(a) % 2 != 0:
            print('b=2 odd')
            if a[0:str1_len] == a[str1_len+1:len(a)]:
                b = 3
                return ('String is symmetrical')
    else: return False




# Reverse words in a given String

def reverse_words(a):
    print(a[::-1])



# Ways to remove i’th character from string


def remove_ith(a,i):
    to_removed = a[i]
    char_list = list(a)

    for j in range(0,len(a)):
        if char_list[j] == to_removed:
            char_list.pop(j)
    return ''.join(char_list)

# Check if a Substring is Present in a Given String
# Words Frequency in String Shorthands
# Convert Snake case to Pascal case
# Find length of a string (4 ways)
# Print even length words in a string
# Accept the strings which contains all vowels
# Count the Number of matching characters in a pair of string
# Remove all duplicates from a given string
# Least Frequent Character in String
# Maximum frequency character in String
# Check if a string contains any special character
# Generating random strings until a given string is generated



if __name__ == '__main__':
    str7 = 'aditya'
    # print(check_palidrome(str3))
    # print(check_sys_pali(str6))
    # reverse_words(str7)
    # (remove_ith(str1,'2'))
    remove_ith(str1,3)
    pass