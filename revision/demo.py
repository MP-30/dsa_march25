# quantity should be greater than 10 and rate should be less then 100

arr = {'quantity': [2,3,4,5,56,6,7,13,13], 'rate':[120,130,104,50,56,60,70,130,90]}

def to_check(arr):
    result = {}
    for i in range(0,len(arr['quantity'])):
        if arr['quantity'][i] > 10 and arr['rate'][i] < 100:
            result[arr['quantity'][i]] = arr['rate'][i]
    print(result)
            

to_check(arr)