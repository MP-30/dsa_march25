# Find sum of array

a = [1,2,3,4,5,6]
def sum_arr(a):
    summ = 0
    for i in a:
        summ +=i
    print(summ)



# Find largest element in an array

b = [2,3,4,5,6,7,8]
def largst(a):
    largest = 0
    for i in b:
        if i > largest:
            largest = i
    print(largest)


# Program for array rotation

c = [1,2,3,4,5,6]
def rotate_arr1(a):
    c1 = c[::-1]
    # for i in range(0,len(a)):
    #     c1.append(c[i])

    print(c1)

c = [1,2,3,4,5,6]
def rotate_arr(a):
    c1 = c[::-1]
    # for i in range(0,len(a)):
    #     c1.append(c[i])

    print(c1)

# Reversal algorithm for array rotation
# Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
#          d = 2
# Output: arr[] = [3, 4, 5, 6, 7, 1, 2]

ar = [1,2,3,4,5,6,7]

d =2
def rotate_second_arr(ar,d):
    for i in range(0,d):
        value_to_remove=ar[0]
        ar.remove(ar[0])
        ar.append(value_to_remove)
    print(ar)



# Split the array and add the first part to the end
ar1 = [1,2,3,4,5,6,7]
d1 = 2
def split_Arr(ar1,d1):
    arr1 = ar1[:d1]
    arr2 = ar1[d1:]
    result = arr2 + arr1
    print(result)



# Find reminder of array multiplication divided by n


arr2 = [1,2,3,4,5,6,7,8]

n1 = 11

def reminder_arr(arr2,n1):
    multi = 1
    for i in arr2:
        multi *=i
    result = multi%n1
    print(result)


# Check if given array is Monotonic

arr3 = [9,8,7,6,5,4,3,2]

def check_monotonic(arr3):
    value = 0
    if arr3[0] < arr3[1]:
        value = arr3[0]
        for i in range(1,len(arr3)):
            if arr3[i] >= value:
                value = arr3[i]
            else:
                return False
    elif arr3[0] > arr3[1]:
        value = arr3[0]
        for i in range(1,len(arr3)):
            if arr3[i] <= value:
                value = arr3[i]
            else:
                return False
   
    return True

if __name__ == '__main__':
    # sum_arr(a)
    # largst(b)
    # rotate_arr(c)
    # rotate_second_arr(ar,d)
    # split_Arr(ar1,d1)
    # reminder_arr(arr2,n1)
    print(check_monotonic(arr3))
    pass