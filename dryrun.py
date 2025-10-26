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


set1 = {1, 2, 4}
set2 = {4, 5, 6}
print(len(set1 + set2))