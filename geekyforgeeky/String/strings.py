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
    list1 = [7,81,2,3,4,5,6]
    for j in range(len(list1)-1, -1,-1):
        if list1[j] == i:
             list1.pop(j)
             
    return list1

# Check if a Substring is Present in a Given String

mainString = 'aditya'
subString = 'it'
def check_substring(mainString, subString):
    # if subString in mainString:
    #     print(True)
    result = False
    convertStrMain = list(mainString)
    convertStrSub = list(subString)
    length_of_sub = len(convertStrSub)
    for i in range(0,len(convertStrMain)):
        if convertStrMain[i] == convertStrSub[0] and (i+length_of_sub)-1 <= len(convertStrMain):
            for j in range(0,length_of_sub):
                if convertStrMain[j+i] != convertStrSub[j]:
                    result = False
                else:
                    result = True
    print(result)
                
    




# Words Frequency in String Shorthands


from collections import Counter
string1 = 'Helllo Hello hello i an an am aditya sing singh singh'
def check_freq(string1):
    # through inbuild method
    # W_freq = Counter(string1.split())
    # print(W_freq)
    
    dict1 = {}
    new_list = string1.split()
    for i in new_list:
        if i not in dict1:
            dict1[i] = 1
        elif i in dict1:
            dict1[i] +=1
    print(dict1)


# Convert Snake case to Pascal case

snake_str = "my_function_name"
def convert_snake_pascal(strr):
    new_list = strr.split('_')
    for i in range(0,len(new_list)):
        new_list[i] = (new_list[i].capitalize())
    print(''.join(new_list))


# Find length of a string (4 ways)

to_length = 'adityaisagoodman'

def find_length(to_length):
    count = 0
    for i in to_length:
        count +=1
    print(count)

# Print even length words in a string

to_even = 'I am a very good person and my name is aditya'
def print_even(to_even):
    new_list = to_even.split()
    final_answer = []
    for i in new_list:
        if len(i) % 2 == 0:
            final_answer.append(i)
    print(final_answer)


# Accept the strings which contains all vowels

to_vowels = 'anvdjkshfjkdejkljgklsdiou'

def check_vowels(to_vowels):
    v = ['a','e','i','o','u']
    for i in v:
        if i not in to_vowels:
            return(False)
    return(True)
            


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
    # print(remove_ith(str1,3))
    # check_substring(mainString, subString)
    # check_freq(string1)
    # convert_snake_pascal(snake_str)
    # find_length(to_length)
    # print_even(to_even)
    print(check_vowels(to_vowels))
    pass