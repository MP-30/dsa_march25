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
a = [1,2,3]
b = [3,4,5]
c = [4,5,6]
def clear_list(a,b,c):
    a.clear()
    c = []
    del b[:]
    print(a)
    print(b)
    print(c)

# Reversing a List
def reverse_list(lt):
    length = len(lt)//2
    for i in range(0,length):
        lt[i], lt[-(i+1)] = lt[-(i+1)], lt[i]
    print(lt)   



# Find sum of elements in list

def sum_of_lst(lt):
    sum = 0
    for i in lt:
        sum += i
    print(sum)


# Multiply all numbers in the list

def mul_of_lst(lt):
    mul = 1
    for i in lt:
        mul *= i
    print(mul)


# Find smallest number in a list

def smallst(lt):
    smallest_num = lt[0]
    for i in lt:
        if smallest_num > i:
            smallest_num = i
        else:pass
    print(smallest_num)

# Find largest number in a list


def largest(lt):
    largest_num = lt[0]
    for i in lt:
        if largest_num < i:
            largest_num = i
        else:pass
    print(largest_num)


# Find second largest number in a list

def second_lsrgest(lt):
    largest_num = 0
    second_largest = 0
    for i in lt:
        if largest_num < i:
            largest_num = i
    for j in lt:
        if second_largest < j and j != largest_num:
            second_largest = j
            
        else:pass
    print(largest_num)
    print(second_largest)


if __name__ == '__main__':
    lst = [2,3,4,5,6,1,7,8,9]
    
    # interchange(lst)
    # swaping(lst)
    # find_length(lst)
    # find_element(lst, 4)
    # clear_list(a,b,c)
    # reverse_list(lst)
    # sum_of_lst(lst)
    # mul_of_lst(lst)
    # smallst(lst)
    # largest(lst)
    second_lsrgest(lst)
    pass