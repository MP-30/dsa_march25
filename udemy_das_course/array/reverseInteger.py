num = 1234
def reverse_number(num):
    num1 = list(str(num))
    for i in range(0,(len(num1)//2)+1):
        num1[i], num1[-(i+1)] = num1[-(i+1)] , num1[i]
    print(int(''.join(num1))) 
    

def reverse_number1(num):
    lst = []
    while num > 0:
        remainder =  num%10
        num = num//10
        lst.append(str(remainder))
    print(int(''.join(lst)))

def reverse_number2(num):
    reversed = 0
    while num > 0:
        remainder =  num%10
        num = num//10
        reversed = reversed * 10 + remainder
    print(reversed)

if __name__ == '__main__':
    # reverse_number(num)
    # reverse_number1(num)
    reverse_number2(num)