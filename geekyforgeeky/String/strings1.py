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
# Replace duplicate Occurrence in String
# Replace multiple words with K
# Permutation of a given string using inbuilt function
# Check for URL in a String
# Execute a String of Code
# String slicing to rotate a string
# String slicing to check if a string can become empty by recursive deletion
# Counter| Find all duplicate characters in string
# Replace all occurrences of a substring in a string



if __name__ == '__main__':
    # find_greater(str1, k)
    # remove_ith(str2,i)
    # split_join(str3)
    print(check_binary(str4))
    pass