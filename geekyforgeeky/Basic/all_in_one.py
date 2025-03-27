# Add two numbers

def add_two(a,b):
    print(a+b)
# Maximum of two numbers

def max_of_two(a,b):
    print(max(a,b))
# Factorial of a number

def fact(n):
    list = []
    result = 1
    while n > 0:
        list.append(n)
        result = result * n
        n -=1
    print(list)
    print(result)


# Find simple interest

# A = P (1 + rt)
# A	=	final amount
# P	=	initial principal balance
# r	=	annual interest rate
# t	=	time (in years)

def si(P, r, t):
    A = int(P)*(1+ (int(r)*int(t)))
    print(A)



# Find compound interest

# CI = P(1 + r/100)n – P


# Where,


# P = Initial Principal Amount
# r = Annual Interest Rate
# n = Number of Times Interest is Compounded
# t = Number of Years


def ci(P, r, n, t):
    a = P * (1+ (r/(100* n)))**(n * t)
    com_inst = a - P
    print(com_inst)



# Check Armstrong Number
# which means some of each dight is equal to its own number

def arms(numb):
    str_num = str(numb)
    leng_of_num = len(str_num)
    lst_of_num = []
    final_sum = 0
    for i in str_num:
        lst_of_num.append(int(i))
    for j in lst_of_num:
        final_sum += j ** leng_of_num
    if final_sum == numb:
        print('Yes')
    else:
        print('No')


# Find area of a circle

def circle_area(r):
    area_of_circle = 3.14 * (r **2)
    print(area_of_circle)

# Print all Prime numbers in an Interval

def all_prime(a,b):
    lst = []
    for i in range(a,b+1):
        if i ==2:
            lst.append(i)
        elif i >2:
            is_prime = True
            for j in range(2, int(math.sqrt(i)+1)):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                lst.append(i)
    print(lst)

# Check whether a number is Prime or not

import math
def prime_num(n):
    if n <=1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n > 2:
        for i in range(3, int(math.sqrt(n)+1),2):
            if n % i == 0:
                return(False)
    return True

# N-th Fibonacci number

def nth_fibo(n):
    if n <=2:
        return(1)
    lstt = [0,1]
    while len(lstt) < n:
        lstt.append(lstt[-1] + lstt[-2])
    return(lstt[n-1])
    # print(lstt)

# Check if a given number is Fibonacci number?


def nth_fibo(n):
    if n>0:
        lstt = [0,1]
        while lstt[-1] <= n:
            lstt.append(lstt[-1] + lstt[-2])
        # return(lstt[n-1])
        # print(lstt)
        if n in lstt:
            print('Yes')
        else: print('No')
    else:print('No')
# Nth multiple of a number in Fibonacci Series

def nth_multiple_of_fibo(k, n):
    first = 0
    second = 1
    count = 0
    while True:
        next = first + second
        first, second = second, next

        if next % k == 0:
            count +=1
            if count == n:
                return next
            

# Print ASCII Value of a character

def ascii_value(a):
    print(f'value of ascii is {ord(a)}')

# Sum of squares of first n natural numbers

def squar_natural(n):
    lst = []
    for i in range(1,n+1):
        lst.append(i*i)

    print(lst)

# Cube sum of first n natural numbers

def cube_natural(n):
    lst = []
    for i in range(1,n+1):
        lst.append(i*i*i)

    print(lst)

if __name__ == '__main__':
    # add_two(1,2)
    # max_of_two(2,3)
    # fact(5)
    # si(5000, 10, 5)
    # ci(2, 12, 21, 2)
    # arms(1634)
    # circle_area(2)
    # prime_num(3)
    # all_prime(2,8)
    # print(nth_fibo(12))
    # nth_fibo(144)
    # print(nth_multiple_of_fibo(4,3))
    # ascii_value('c')
    # squar_natural(9)
    cube_natural(8)
    pass