'''
Given an array, find the total sum of all possible subarray
'''

arr = [1,2,3]
def solve1(arr):
    summ = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            summ += sum(arr[i:j+1])
    return summ

def solve2(arr):
    sum = 0
    i = 0
    while i < len(arr):
        local_sum = 0
        j = i
        while j <len(arr):
            local_sum += arr[j]
            sum += local_sum
            j +=1
        i +=1
    return  sum
# check with kartik
def solve3(arr):
    total_sum= 0
    prefix = [0]
    for k in range(len(arr)):
        prefix.append(prefix[-1]+arr[k])
    print (prefix)
    i = 0
    while i < len(arr):
        j = i
        while j < len(arr):
            summ = prefix[j+1] - prefix[i]
            total_sum += summ
            j +=1
        i +=1
    return total_sum

def solve4(arr):
    number = len(arr)
    start = 1
    result = 0
    while number >0:
        value = number * start
        result += (arr[start -1] * value)
        number -= 1
        start +=1
    return  result

def solve(arr):
    total_sum = 0
    for i in range(len(arr)):
        contribute = arr[i] * (i+1) * (len(arr) -i)
        total_sum += contribute

    return  total_sum

print(solve(arr))