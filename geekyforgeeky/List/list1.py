# Interchange first and last elements in a list

def interchange(l):
    l[0],l[-1] = l[-1],l[0]
    print(l )


# Swap two elements in a list

def swaping(l):
    l[2],l[3] = l[3],l[2]
    print(l )
    

# Ways to find length of list

def find_length(l):
    count = 0
    for i in l:
        count +=1
    print(count)




# Ways to check if element exists in list

def find_element(l, n):
    if n in l:
        print("Yes")


# Different ways to clear a list
# Reversing a List
# Find sum of elements in list
# Multiply all numbers in the list
# Find smallest number in a list
# Find largest number in a list
# Find second largest number in a list

if __name__ == '__main__':
    lst = [1,2,3,4,5,6,7,8,9]
    # interchange(lst)
    # swaping(lst)
    # find_length(lst)
    find_element(lst, 4)
    pass