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

old_students = ['Manoj', 'Raju', 'Shiva' ]

new_students = ['Akhil', 'Balu', 'Chitra']

old_students.extend(new_students)
print(old_students)