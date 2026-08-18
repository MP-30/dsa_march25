# Print anagrams together using List and Dictionary

def anagrams_list():
    dict = {} 
    a = ['bat', 'nat', 'tan', 'ate', 'eat', 'tea']
    b = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
    for i in a:
        srt = (''.join(sorted(i)))
        if srt not in dict:
            dict[srt] = [i]
        elif srt in dict:
            dict[srt].append(i)
    print(dict)


# K’th Non-repeating Character using List Comprehension and OrderedDict

s = "geeksforgeeks"
k = 3
from collections import Counter
def kTh_nonRepeated(s,k):
    dictt = (dict(Counter(s)))
    new_list = [chr for chr, countt in dictt.items() if countt == 1]
    print(new_list[k-1])


# Check if binary representations of two numbers are anagram

def check_binary():
    a = 8
    b = 4
    bin1 = bin(a)[2:]
    bin2 = bin(b)[2:]
    
    zeros = abs(len(bin1) - len(bin2))
    if zeros >0:
        if (len(bin1) > len(bin2)):
            bin2 = zeros * '0' + bin2
        elif (len(bin1) < len(bin2)):
            bin1 = zeros * '0' + bin1
    dict1 = (dict(Counter(bin1)))
    dict2 = (dict(Counter(bin2)))
    
    if dict1 == dict2:
        print('Yes')
    else: print('No')
        

# Counter to find the size of largest subset of anagram words

'''
Input: 
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3

Input: 
cars bikes arcs steer 
Output: 2
'''
inp1 = 'ant magenta magnate tan gnamate'
inp2 = 'cars bikes arcs steer'
def counter_subset(inp):
    dictt = {}
    inpp = ((inp.split()))
    for i in inpp:
        list_inp = (''.join(sorted(i)))
        if list_inp not in dictt:
            dictt[list_inp] = [i]
        elif list_inp in dictt:
            dictt[list_inp].append(i)
    max_size = 0
    for j in dictt.values():
        if len(j) > max_size:
            max_size = len(j)
    print(max_size)
    



# Remove all duplicates words from a given sentence

s3 = "Geeks for Geeks"

def remove_dup(stt):
    new_lst =  ([new_list for new_list in stt.split()])
    result = dict(Counter(new_lst))
    final_result = result.keys()
    print(list(final_result))
    

# Dictionary to find mirror characters in a string


s4 = 'paradox'
N1 = 3

N2 = 6
s5 = 'pneumonia'

def find_mirror(n,s):
    main_str = 'abcdefghijklmnopqrstuvwxyz'
    new_str = []
    for i in s[n+1:]:
        for j,k in enumerate(main_str):
            if i == k:
                print(j)
                new_str.append(main_str[25-j])
    
    print(s[:n+1] + ''.join(new_str))

# Counting the frequencies in a list using dictionary
a5 = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

def count_freq(a5):
    print(dict(Counter(a5)))



# Convert a list of Tuples into Dictionary

a6 = [("a", 1), ("b", 2), ("c", 3)]

def convert_to_dict(a6):
    new_dict = {}
    for i in a6:
        new_dict[i[0]] = i[1]
    print(new_dict)

# Counter and dictionary intersection example (Make a string using deletion and rearrangement)

'''
Given two strings, find if we can make first string from second by deleting some characters from second and rearranging remaining characters. 

Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : Not Possible

Input : s1 = GeeksforGeeks
      : s2 = rteksfoGrdsskGeggehes
Output : Possible
'''
q1 = 'ABHISHEKsinGH'
q2 = 'gfhfBHkooIHnfndSHEKsiAnG'

q3 = 'Hello'
q4 = 'dnaKfhelddf'

q5 = 'GeeksforGeeks'
q6 = 'rteksfoGrdsskGeggehes'

def check_dct(str1, str2):
    dict1 = dict(Counter(str1))
    dict2 = dict(Counter(str2))
    
    
    for char, count in dict1.items():
        if char not in dict2 or dict2[char] < count:
            return False
    return True
    
        
        


# Dictionary, set and counter to check if frequencies can become same


str11 = 'xxxxyyzz'
def can_frequencies_be_same(str11):
    counts = Counter(s)
    frequencies = list(counts.values())
    n = len(frequencies)

    # If all frequencies are already the same
    if len(set(frequencies)) == 1:
        return True

    # Try removing one occurrence of each character
    for char_to_remove in counts:
        temp_counts = counts.copy()
        temp_counts[char_to_remove] -= 1
        if temp_counts[char_to_remove] == 0:
            del temp_counts[char_to_remove]

        temp_frequencies = list(temp_counts.values())
        if not temp_frequencies:  # String becomes empty after removal
            return True
        if len(set(temp_frequencies)) == 1:
            return True

    # Try removing one character to make all frequencies equal to 1
    if len(set(frequencies)) == n and 1 in frequencies and all(f == 1 or f == 2 for f in frequencies) and frequencies.count(2) <= 1:
        return True

    # Try removing one character to make all frequencies equal to the minimum frequency
    min_freq = min(frequencies)
    possible = False
    for char in counts:
        temp_counts = counts.copy()
        if temp_counts[char] > min_freq:
            temp_counts[char] -= 1
            temp_freqs = set(temp_counts.values())
            if len(temp_freqs) == 1 and min_freq in temp_freqs:
                possible = True
                break

    if possible:
        return True

    # Try removing one character to make all frequencies equal to the maximum frequency - 1
    max_freq = max(frequencies)
    possible = False
    for char in counts:
        temp_counts = counts.copy()
        if temp_counts[char] == max_freq:
            temp_counts[char] -= 1
            if temp_counts[char] == 0:
                temp_freqs = set(temp_counts.values())
                if len(temp_freqs) == 1 and (not temp_freqs or max_freq - 1 in temp_freqs):
                    possible = True
                    break
            else:
                temp_freqs = set(temp_counts.values())
                if len(temp_freqs) == 1 and max_freq - 1 in temp_freqs:
                    possible = True
                    break
    if possible:
        return True

    return False     
    


# Scraping And Finding Ordered Words In A Dictionary

list_to_check = ['aau','abbe','abbey','abbot','abbott','abc','abe','abel','abet','abo','abort','accent','accept']

def check_order(list_to_check):
    dictt = {}
    for i in list_to_check:
        if (''.join(sorted(i))) == i:
            dictt[i] = 'yes'
        elif (''.join(sorted(i))) != i:
            dictt[i] = 'no'
    print(dictt)
    
            

# Possible Words using given characters

Dict = ["go","bat","me","eat","goal","boy", "run"]

def possibility(words):
    arr = ['e','o','b', 'a','m','g', 'l']
    result = {}
    for word in words:
        for char in word:
            if char not in arr:
                result[word] = False
                break
        else:
            result[word] = True
    print(result)




# Keys associated with Values in Dictionary

# Example inputs
test_dict1 = {'abc': [10, 30], 'bcd': [30, 40, 10]}
test_dict2 = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

# Expected outputs
output1 = {10: ['abc', 'bcd'], 30: ['abc', 'bcd'], 40: ['bcd']}
output2 = {1: ['is', 'gfg'], 2: ['gfg', 'best'], 3: ['gfg'], 4: ['is', 'best']}

def associated_dict(test_dict, output):
    result = {}
    for i , j in test_dict.items():
        for k in j:
            if k not in result:
                result [k] = [i]
            elif k in result:
                result[k].append(i)
    print(result)



if __name__ == '__main__':
    # anagrams_list()
    # kTh_nonRepeated(s,k)
    # check_binary()
    # counter_subset(inp1)
    # remove_dup(s3)
    # find_mirror(N1,s4)
    # count_freq(a5)
    # convert_to_dict(a6)
    # print(check_dct(q1, q2))
    # can_frequencies_be_same(str11)
    # check_order(list_to_check)
    # posibility(Dict)
    associated_dict(test_dict2, output1)
    pass