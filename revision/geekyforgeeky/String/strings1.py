# Find words which are greater than given length k

str1 = "hello geeks for geeks is computer science portal" 
k = 4

def find_greater(str1, k):
    list1 = str1.split()
    result = []
    for i in list1:
        if len(i) > k:
            result.append(i)
    print(result)
            

# Removing i-th character from a string

i = 3
str2 = 'aditya'
def remove_ith(str2,i):
    work_list = list(str2)
    for j in range(len(work_list)-1,-1,-1):
        if j == i:
            work_list.pop(i)
    print(''.join(work_list))



# Split and join a string

str3 = 'aditya'
def split_join(str3):
    list1 = str3.split()
    print(''.join(list1))


# Check if a given string is binary string or not
str4 = "101010000111"
def check_binary(str4):
    from_check = ['0','1']
    for i in range(0,len(str4)):
        if str4[i] not in from_check:
            return False

    return True
            


# Find uncommon words from two Strings
from collections import Counter
s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"

def find_uncommon(s1,s2):
    count = Counter(s1.split() + s2.split())
    uncommon = [words for words in count if count[words] == 1]
    print(uncommon)



# Replace duplicate Occurrence in String

test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better . ' 
 
repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

def replace_duplicate(test_str, repl_dict):
    new_list = test_str.split()
    
    for i, j in repl_dict.items():
        print(i,j)
        for k in range(0,len(new_list)):
            if i == new_list[k]:
                new_list[k] = j
    print(' '.join(new_list))
                
                

# Replace multiple words with K

text = "apple orange banana"
words_to_replace_with_K = ['apple', 'banana']

def replace_multiple(text, words_to_replace_with_K):
    new_list = text.split()
    for i in range(0,len(new_list)):
        if new_list[i] in words_to_replace_with_K:
            new_list[i] = 'K'
    print(' '.join(new_list))


# Permutation of a given string using inbuilt function

import itertools

s2 = 'ABC'
def generate_permutation(s2):
    l = []
    for i in itertools.permutations(s2):
        l.append(''.join(i))
    print(l)
        
    
    
# Check for URL in a String
s3 = 'My Profile: https://auth.geeksforgeeks.org/user/Prajjwal%20/articles in the portal of https://www.geeksforgeeks.org/'

def check_url(s3):
    new_list = s3.split()
    urls_list = []
    for i in new_list:
        if i[:8] == 'https://':
            urls_list.append(i)
            
    print(urls_list)


# Execute a String of Code
code = 'x = 5\ny = 10\nprint(x + y)'
def exec_function(code):
    exec(code)



# String slicing to rotate a string
s4 = 'GeeksforGeeks'
d = 2
def string_rotating(s4, d):
    new_string =  s4[d:] + s4[:d+1] 
    print(new_string)


# String slicing to check if a string can become empty by recursive deletion


s5 = 'geeksforgeeks'



# Counter| Find all duplicate characters in string

s6 = 'geeksforgeeks'
def find_dupli_char(s6):
    new_list = Counter(list(s6))
    duplicate = []
    for i,j in new_list.items():
        if j > 1:
            duplicate.append(i)
    print(duplicate)
    
    
# Replace all occurrences of a substring in a string

s7 = 'python is a very good language'
a1 = 'c++'

def replace_string(s7,a1):
    new_list = s7.split()
    for i in range(0,len(new_list)):
        if new_list[i] == 'python':
            new_list[i] = a1
    print(' '.join(new_list))




if __name__ == '__main__':
    # find_greater(str1, k)
    # remove_ith(str2,i)
    # split_join(str3)
    # print(check_binary(str4))
    # find_uncommon(s1,s2)
    # replace_duplicate(test_str, repl_dict)
    # replace_multiple(text, words_to_replace_with_K)
    # generate_permutation(s2)
    # check_url(s3)
    # exec_function(code)
    # string_rotating(s4, d)
    # find_dupli_char(s6)
    replace_string(s7,a1)
    pass