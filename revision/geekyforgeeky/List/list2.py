# Find N largest elements from a list

def n_largest(n,lst):
    lst.sort()
    print(lst[n])
    print(lst)


# Even numbers in a list

def find_even(lst):
    new_lst = []
    for i in lst:
        if i % 2 ==0:
            new_lst.append(i)
    print(new_lst)



# Odd numbers in a List
def find_odd(lst):
    new_lst = []
    for i in lst:
        if i % 2 !=0:
            new_lst.append(i)
    print(new_lst)


# Print all even numbers in a range

def even_in_range(a,b,lst):
    new_lst = []
    for i in range(a,b+1):
        if lst[i] %2 == 0:
            new_lst.append(lst[i])
    print(new_lst)


# Print all odd numbers in a range



def odd_in_range(a,b,lst):
    new_lst = []
    for i in range(a,b+1):
        if lst[i] %2 != 0:
            new_lst.append(lst[i])
    print(new_lst)


# Print positive numbers in a list

def print_positive(lst):
    new_lst = []
    for i in lst:
        if i > 0:
            new_lst.append(i)

    print(new_lst)

# Print negative numbers in a list


def print_negative(lst):
    new_lst = []
    for i in lst:
        if i < 0:
            new_lst.append(i)

    print(new_lst)


# Print all positive numbers in a range


def all_positive_in_range(a,b,lst):
    new_lst = []
    for i in range(a,b+1):
        if lst[i] > 0:
            new_lst.append(lst[i])
    print(new_lst)


# Print all negative numbers in a range

def all_negative_in_range(a,b,lst):
    new_lst = []
    for i in range(a,b+1):
        if lst[i] < 0:
            new_lst.append(lst[i])
    print(new_lst)


# Remove multiple elements from a list

def multiple_element(lst):
    dict = {}
    for i in lst:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1

    new_lst = []
    for j in dict:
        new_lst.append(j)
    print(new_lst)
    # print(dict)




if __name__ == '__main__':
    lst = [11,1,1,2,3,4,5,-3,-2,6,7,8,8,8,8,9]
    # n_largest(5,lst)
    # find_even(lst)
    # find_odd(lst)
    # even_in_range(1,5,lst)
    # odd_in_range(0,5,lst)
    # print_positive(lst)
    # print_negative(lst)
    # all_positive_in_range(1,10,lst)
    # all_negative_in_range(1,10,lst)
    multiple_element(lst)
    pass