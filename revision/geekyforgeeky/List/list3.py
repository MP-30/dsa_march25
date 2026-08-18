# Remove empty List from List

def remove_empty_list(lst):
    to_print = []
    for i in range(0,len(lst)):
        if len(lst[i]) != 0:
            to_print.append(lst[i])
    print(to_print)

# Cloning or Copying a list

def clone_and_copy(lst):
    a = lst
    print(a)


# Count occurrences of an element in a list

def find_occurrences(lst):
    dict = {}
    for i in lst:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] +=1
    print(dict)

# Remove empty tuples from a list

def remove_tuples(lst):
    new_list = []
    for i in lst:
        if len(i) >0:
            new_list.append(i)

    print(new_list)



# Print duplicates from a list of integers

def remove_duplicates(lst):
    dict = {}
    for i in lst:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] +=1
    res = dict.keys()
    print(res)



# Find Cumulative sum of a list

def cumulative(lst):
    new_list = []
    for i in range(1,len(lst)):
        to_add = sum(lst[0:i])
        new_list.append(to_add)
    print(new_list)


# Sum of number digits in List

def sum_of_digits(lst):
    summ = 0
    for i in lst:
        if type(i) is int:
            summ += i
    print(summ)

# Break a list into chunks of size N

def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))




# Sort the values of first list using second list


if __name__ == '__main__':
    L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    list1 = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]
    list2 = [1,1,2,3,4,4,5,2,6,8,3,9]
    list3 = [1,2,3,4,'r',5,3,2,1,'t']
    # remove_empty_list(list1)
    # clone_and_copy(list1)
    # find_occurrences(list2)
    # remove_tuples(L)
    # remove_duplicates(list2)
    # cumulative(list2)
    # sum_of_digits(list3)
    pass