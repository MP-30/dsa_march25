# strr = 'adityai'
# listt = list(strr)
# for i in range(0,len(listt)//2):
#     listt[i], listt[-(i+1)] = listt[-(i+1)], listt[i]
# print(''.join(listt))

# def delete_conso(data):
#     aa = ['A','E','I','O','U','a','e','i','o','u']
#     result = ''
#     for i in data:
#         if i in aa:
#             result += i
#     print(result)
# delete_conso('Python and Data Science')

# def only_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
            

# def sum_prime(n):
#     summ = 0
#     for nm in range(2,n+1):
#         if only_prime(nm):
#             summ += nm
#     print(summ)
    
# sum_prime(15)


# iterator
# class Counter:
#     def __init__(self,n):
#         self.n = n
#         self.current = n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current < self.n:
#             self.current +=1
#             return self.current
#         raise StopIteration
    
    
    # context manageer
# class FileOpener:
#     def __init__(self,name):
#         self.name = name
#     def __enter__(self):
#         self.file = open(self.name)
#         return self.file
    
#     def __exit__(self, exc_type, exc_val, exe_tb):
#         self.file.close()

# generator

# def sqares(n):
#     for i in range(n):
#         yield (i*i)
        
        
        
# decorator

# def logger(func):
#     def wrapper(*a, **kw):
#         a = func(*a, **kw)
#         return(a)
#     return wrapper

# @property

# class Person:
#     def __init__(self,age):
#         self.age = age
        
#     @property
#     def age(self):
#         return self.age
#     @age.setter
#     def age(self,v):
#         self.age = v

        
        
        
# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
        
        
# def print_digits(n):
#     while n >0:
#         print(n%10, end=" ")
#         n = n//10
        
# print_digits(459)

# def sum_num(n):
#     summ = 0
#     while n > 0 :
#         summ += (n%10)
#         n = n//10
#     print(summ)
    
# sum_num(123)


# def add_last(n,d):
#     print((n*10)+d)
    
# add_last(234,8)

# def reverse_print(n):
#     l = abs(n)
#     total_digits = 0
#     m = l
#     while l > 0:
#         l = l //10
#         total_digits +=1
#     reverse_num = 0
#     while m >0:
#         reverse_num += (m % 10) * 10 **(total_digits-1)  
#         m = m //10
#         total_digits -=1
#     if n < 0:
#         print(f"-{reverse_num}")
#     else:
#         print(reverse_num)
    
# reverse_print(-123)


# def star(n):
#     for i in range(1,n+1):
#         print('* ' * i)
            
# star(5)

# i = 0

# while i <=5:
#     if i %2:
#         pass
#     else:print(i,end=" ")
#     i +=1
    
# output = [0,2,4]

# i = 0
# j = 0
# while i <=2:
#     if j %2:
#         j +=1
#     print(i, ":", j, end=" ")
#     j +=1
#     i +=1

# a = 100001
# b = 0
# while a > 0:
#     b = b * 10 + a % 10
#     a = a // 10
# print(b)
# if a == b :
#     print('YES')
# else: print('No')

# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output

#     n = int(input())
#     for i in range(0,n):
#         print(f"*{" "*(n-2)}*")

# if __name__ == '__main__':
#     main()

# A = input()
# a = (A.split(' '))
# num = []
# for i in a:
#     num.append(int(i))
# smallest = min(num)
# hcf = 0
# for i in range(1,smallest+1):
#     if (num[0]% i ==0) and (num[1]%i ==0):
#         hcf = i
# print(hcf)

# name:int = 9

# def multiple_print(s, n = 1):
#     print(s * n, end='')
#     print() # this prints new line i.e. \n

# multiple_print('Hello', 2)
# multiple_print('Hello')

# def sequence(n):
#     '''input: n = A single integer for the range where n is inclusive
#        output: First Print from 1 to N and new line Print from N to 1'''
#     a = int(input())
#     b = int(input())
#     for i in range(1,b+1):
#         print(i,end="")
#     for j in range(b,0,-1):
#         print(j,end="")
#     # YOUR CODE GOES HERE
# sequence(10)


# a = input().split()
# arr = a[1:]
# print(arr)
# count = 0
# for i in arr:
#     if i != ' ':
#         count += int(i)
# print(count)    



# count = 0
# for i in a:
    
    
# def swap(n_list):
#     n_list[-1], n_list[0] = n_list[0],n_list[-1]
#     return n_list
# print(swap([12,41,29,32,7]))

# old_students = ['Manoj', 'Raju', 'Shiva' ]

# new_students = ['Akhil', 'Balu', 'Chitra']

# old_students.extend(new_students)
# print(old_students)


# a = [1,6,2,3,8,4,9,2]
# def check(a):
#     maxx = 0
#     for i in a:
#         if i > maxx:
#             maxx = i
#     print(maxx)
    
# check(a=a)


# print(float('-inf'))
# print(float('inf'))

# a = [23,45,78,12,67,90]

# def check(a,n):
#     for i in range(n):
#          a.append(a[0])
#          a.pop(0)
#     print(a)
# check(a,n=2)

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]
#      ]
# b = [[9,8,7],
#      [6,5,4],
#      [3,2,1]
#      ]

# def check(a,b):
#     for i in range(len(a)):
#         for j in range(len((a)[0])):
#             a[i][j] = a[i][j] + b[i][j]
#     print(a)
# check(a,b)

# def nn():
#     n = int(input())
#     a = list(map(int,(input()).split()))
#     x = (input())
#     for j in range(len(a)-1,-1,-1):
#         if a[j] == x:
#             a.pop(a[j])
#     return a

# print(nn())


# a = list(map(int, input().split()))
# print(a[1:])

# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     num_of_element = int(input())
#     arr = list(map(int, input().split()))
#     x = int(input())
    
#     x = x-1
#     x = -1 * x
#     print(x)
#     for i in range(len(arr)-1,-1,-1):
#         if i == x:
#             arr.pop(i)
#     print(arr)
    
# main()

# a = [292, 658, 616, 208, 544, 39, 33, 736, 203, 996, 558, 91, 468, 449, 536, 403, 59, 613, 520, 714, 333, 696, 527, 451, 576, 78, 315, 183, 661, 402, 481, 952, 59, 96, 160, 954, 486, 544, 689, 689, 892, 599, 131, 359, 47, 18, 113, 457, 982, 633, 170, 315, 680, 48, 117, 256, 477, 783, 438, 137, 185, 270, 441, 595, 717, 600, 549, 202, 589, 242, 386, 539, 372, 745, 937, 741, 209, 394, 723, 841, 563, 389, 521, 963, 505, 128, 439, 640, 917, 928, 176, 186, 368, 770, 254, 967, 670, 455, 461, 611, 697, 847, 501, 420, 943, 438, 513, 503, 831, 235, 344, 745, 623, 216, 707, 479, 343, 498, 118, 611, 425, 293, 796, 792, 415, 401, 110, 436, 855, 922, 398, 903, 120, 899, 675, 62, 336, 187, 565, 518, 421, 260, 262, 395, 827, 321, 873, 521, 818, 343, 131, 594, 987, 278, 385, 753, 678, 846, 189, 532, 767, 938, 787, 887, 836, 461, 300, 523, 999, 216, 40, 771, 475, 654, 165, 301, 974, 389, 821, 143, 731, 303, 736, 70, 580, 120, 822, 257, 965, 10, 141, 83, 300, 927, 969, 487, 739, 269, 10, 89, 484, 401, 859, 3]

# for i in a:
     
# num = int(input())
# a = 1
# mx = []
# result = []
# for _ in range(num):
#     b = list(map(int, input().split()))
#     mx.append(b)
# for i in range(1,len(mx)+1):
#     if i %2 != 0:
#         for j in range(num):
#             result.append(mx[i-1][j])
#     elif i % 2 ==0:
#         for j in range(num-1,-1,-1):
#             result.append(mx[i-1][j])
            
# for i in result:
#     print(i,end=" ")

# length = int(input())
# arr = []
# result = []
# for _ in range(length):
#     a = list(map(int, input().split()))
#     arr.append(a)
# for j in range(length):
#     for i in range(length):
#         result.append(arr[i][j])
# print(arr)
# print(result)

# a = 1,
# print(type(a))
# a = '123'
# print(hex(id(a)))
# b =a.replace('1','4')
# print(hex(id(b)))


# name_lst = ["Vijay", "Vickey"]

# tup = ("Item_1", 0.5, name_lst)

# name_lst.append("Vishal")
# print(tup)


# elements = (10,20,30,40,50,60,70,80)

# print(elements[2:5], elements[:4], elements[3:100])


# tuple1 = (1150, 877, 909)
# print(max(tuple1))

# tuple1[0] = 50


# tt = (1, 2, 3, "Hello", [4, 8, 16], 2, "Hello")
# def odd_even_split_tuple(tup):
#     ''' input:tup-indicates the tuple
#          output:print two tuples one for even indexed and odd indexed in the given output format'''
    
#     # YOUR CODE GOES HERE
#     Odd = []
#     Even = []
#     for i in range(1,len(tup)+1):
#         if i % 2 == 0:
#             Even.append(tup[i-1])
#         elif i % 2 != 0:
#             Odd.append(tup[i-1])

#     print(f"Off: {tuple(Odd)}")
#     print(f"Even: {tuple(Even)}")
# odd_even_split_tuple(tt)



class DemoClass:
    '''
    instance method use a self parameter pointing to an instance of the class. They
    can access and modify instance state through self and class state self.__class__.
    These are the most common method in Python classes.
    '''
    def instance_method(self):
        return ("instance method called", self)


    '''
    Class methods use cls paramenter pointing to the class itself. They can modigy class
    level state though cls, but they can't modify individual instance state
    '''
    @classmethod
    def class_method(cls):
        return ("class method called", cls)
    
    
    '''
    Static methods dont take self or cls parameters. They can't modity instance or class state 
    directly, and you will use them for organizational purposes and namespacing.
    '''
    @staticmethod
    def static_method():
        return ("static method clalled")
    
obj = DemoClass()

# print(obj)

# print(obj.instance_method())

# print(obj.class_method())

# print(obj.static_method())

# print(DemoClass.class_method())

# print(DemoClass.static_method())

# print(DemoClass.instance_method())


# def logger(func):
#     def wrapper(* args, ** kwargs):
#         print(f'Calling {func.__name__}')
#         return func(*args, **kwargs)
#     return wrapper

# @logger
# def greet(name):
#     print('Hello {name}')

# greet('aditya')

# from functools import lru_cache

# @lru_cache(maxsize=128)
# def fibonacci(n):
#     if n < 2:
#          return n
#     return fibonacci(n-1) + fibonacci(n-2)

# def cache(func):
#     memory = {}
#     def wrapper(*args):
#         if args not in memory:
#             memory[args] = func(*args)
#         return memory[args]
#     return wrapper


# class Animals:
#     def speak(self):
#         pass
# class Dog(Animals):
#     def speck(self):
#         return 'Woof'
# class Cat(Animals):
#     def speak(self):
#         return 'Meow'


# def count_up_to(n):
#     for i in range(1, n+1):
#         yield i 
        
# for num in count_up_to(3):
#     print(num)

# nums = [1,2,3,4]

# gen = (x * x for x in nums)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(list(gen))

# class InvalidAgeError(Exception):
#     def __init__(self, message= 'Age must be >= 18'):
#         self.message = message
#         super().__init__(self.message)

# import asyncio

# async def task():
#     print('Start')
#     await asyncio.sleep(1)
    
#     print('Done')
    
# asyncio.run(task())

class Singleton:
    _instance = None
    def __new__(cls, *a, **kw):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            
        return cls._instance
    
def find_total(n):
    count = 0
    def is_prime(n):
        if n <2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i ==0:
                return False
        return True
    for i in range(1, n+1):
        if is_prime(i):
            count +=1
    return count
            
# print(find_total(19))

def rotate(a,n=0):
    max_num = max(a)
    count = 0
    for  i in a:
        if i != max_num:
            local_count = max_num - i
            count +=local_count
            
    print(count)
    
A = [2]

def checck(a):
    m = max(A)
    n = 0
    for i in A:
        if i < m and i >n:
            n = i
    if n:
        return n
    else: return (-1)
    
    
    
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A+A
        a = list(A)
        new = a 
        for i in range(len(a)-1,-1,-1):
            if a[i].isupper():
                a.pop(i)
            elif a[i] in ['a','e','i','o','u']:
                a[i] = '#'
        return (''.join(a))
    
    
def hel(a):
    a = list(a)
    for i in range(0,len(a)):
        if a[i].isupper():
            a[i] = a[i].lower()
        elif a[i].islower():
            a[i] = a[i].upper()
        
    return(''.join(a))


def hehe(a):
    count = 0
    for i in range(0,len(a)):
        if a[i] =='b' and i <= len(a)-3:
            if a[i+1] == 'o' and a[i+2] == 'b':
                count +=1
    return (count)

def solve1(A):
        vow = ['a','e','i','o','u','A','E','I','O','U']
        count = 0
        for i in range(0,len(A)):
            if A[i] in vow:
                count += (len(A)-i)
        return count
    
# A = 'anagram'
# print(solve1(A))


def ss(logs):
    result = []
    
    for i in logs:
        for j,k in i.items():
            result0 = []
            for m,n in k.items():
                if m == 'level':
                    result.append(f"[{n}]")
                else:
                    result.append(f"{n}")
                    

def chuc(logs):
    result = []
    for i in logs.values():
        for j in i:
            result.append(j)
    sorted_k = sorted(result, key=lambda dic: dic['timestamp'] )
    for a in sorted_k:
        time = a['timestamp']
        lev = a['level']
        err = a['message']
        print(f"{time} [{lev}] {err}")


# 2024-07-18 10:15:00 [ERROR] Database connection failed
# 2024-07-18 10:24:00 [WARNING] Suspicious login attempt detected
# 2024-07-18 14:00:00 [ERROR] External Authencation Service Down
# 2024-07-18 14:42:00 [INFO] Backup Started
# 2024-07-18 14:47:00 [WARNING] Multiple attempts detected

      
logs = {
        "Database_logs": [
            { "timestamp": "2024-07-18 10:15:00", "level": "ERROR", "message": "Database connection failed" },
            { "timestamp": "2024-07-18 14:42:00", "level": "INFO", "message": "Backup Started" }
        ],
        "Authentication_logs": [
            { "timestamp": "2024-07-18 14:00:00", "level": "ERROR", "message": "External Authentication Service Down" },
            { "timestamp": "2024-07-18 10:24:00", "level": "WARNING", "message": "Suspicious login attempt detected" },
            { "timestamp": "2024-07-18 14:47:00", "level": "WARNING", "message": "Multiple attempts detected" }
        ]
        }

# print(chuc(logs))


def recur(n):
    if n ==0:
        return
    else:
        recur(n-1)
     

# (recur(5))
cache = {}
def  febo(n):
    if cache.get(n) is not None:
        return cache[n]
    if n ==1 or n==2:
        return 1
    elif n ==0:
        return 0
    cache[n-1] = febo(n-1)
    cache[n-2] = febo(n-2)
    return cache[n-1] + cache[n-2]
# print(febo(4))


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0 or A == 1:
            return 1
        ss = Solution()
        ans = A * ss.solve(A-1)
        return ans 
# sss = Solution()
# print(sss.solve(4))

def chuchu(a):
    if a ==2 or a ==1 :
        return 1
    ans = chuchu(a-1) + chuchu(a-2)
    
    return ans

def chichi(a):
    if a ==0:
        print()
        return
    print(a, end=' ')
    chichi(a-1)
    
    
def bar(x,y):
    if y ==0:
        return 0
    
    return (x + bar(x,y-1))

def foo(x,y):
    if y ==0:
        return 1
    return bar(x, foo(x, y-1))

# print(foo(3,5))

def fun(x,n):
    if n==0:
        return 1
    elif (n % 2) == 0:
        return fun(x * x , n//2)
    else:
        return x * fun(x * x, (n-1)//2)
    
# ans = fun(2,10)
# print(ans)

def ssolve(a):
    if a == 0:
        return 0
    return a % 10 + ssolve(a // 10) 
    
    
# print(ssolve(12346))

'''
num = 123
output = 321
'''

def ssolve(num, a = 0):
    if num == 0:
        return a
    a = a*10 + num%10
    a = ssolve(num//10, a)
    return a
    
# print(ssolve(123))
def solve(A):
        st = []
        for i in A:
            if not st:
                st.append(i)
            elif st and st[-1] == i:
                st.pop()
            else:
                st.append(i)
        return (''.join(st))
        
# A = 'abccbc'
# print(solve(A)) 

def rate_limit_stream(timestamps, K, T):
    # Your Code goes here
    from collections import deque
    aa = deque()
    result = []
    for t in timestamps:
        while aa and aa[0] <= t-T:
            aa.popleft()
            
        if len(aa) <K:
            result.append(1)
            aa.append(t)
        else:
            result.append(0)       
    return result
    

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []

        for token in A:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b))  # truncates toward zero

        return stack[-1]
    
    
# -------------


import operator


def solutions(A):
    stack = []
    for i in range(0,len(A)):
        if A[i] == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
        elif A[i] == '-':
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
        elif A[i] == '*':
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)
        elif A[i] == '/':
            right = stack.pop()
            left = stack.pop()
            stack.append(left // right)
        else:
            stack.append(int(A[i]))
    
    return(stack[0])
        
# A =   ["4", "13", "5", "/", "+"]
# solutions(A)



def ssorted(A,B):
    n = len(A)
    
    def find_left():
        low, high = 0, n-1
        ans = -1
       
A = [1, 2, 4, 4, 4, 5, 9]
B = 4

# print(ssorted(A,B))


class Student:
    def __init__(self):
        self.age = 0
        self.name = ""

    def display(self):
        print("My name is", self.name + ". I am", self.age, "years old")


# # Main code
# s1 = Student()
# s1.age = 10

# s2 = s1

# s2.display()


arr1 = [5,11,13,15,21]
arr2 = [2,4,8,10]

def sorted_arr(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i +=1
        else:
            result.append(arr2[j])
            j+=1
    while i < len(arr1):
        result.append(arr1[i])
        i+=1
        
    while j < len(arr2):
        result.append(arr2[j])
        j +=1
        
    return result 
# print(sorted_arr(arr1, arr2))

def mini(A):
    b =sorted(A)
    return(b)

# A = [1,4,10,2,1,5]
# print(mini(A))


# a  = [9,2,8]
# b = [5,6,7]
# if b<a:
#     print(8)
# else:
#     print(9)
    
    
def moveZerosToEnd(A):
    pos = 0 
    for num in A:
        if num != 0:
            A[pos] = num
            pos += 1
    while pos < len(A):
        A[pos] = 0
        pos += 1
    
    return A

def check(a, b):
    def left():
        left = 0
        right = len(a)-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if a[mid] == b:
                ans = mid
                right = mid -1
            elif a[mid] < b:
                left = mid +1
            else:
                right = mid -1
        return ans
    
    def right():
        left = 0
        right = len(a)-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if a[mid] == b:
                ans = mid
                left = mid +1
            elif a[mid] < b:
                left = mid +1
            else:
                right = mid -1
        return ans
    
    return ([left(), right()])
    
# a = [5,7,7,8,8,10]
# b = 8

# print(check(a, b))\
    
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("a", type=int, help='First number')
# parser.add_argument("b", type=int, help='Second number')

# arg = parser.parse_args()

# print("SUm", arg.a + arg.b)


A = [26,32,71,69,84,22,33,37,44]
B = 4
C = 5

def solveOne(A, B, C):
    a = A[:B]
    b = A[B:C+1]
    if C < len(A)-1:
        c = A[C+1:]
    else:
        c = []
    return(a+sorted(b)+c)
    
print(solveOne(A,B,C))