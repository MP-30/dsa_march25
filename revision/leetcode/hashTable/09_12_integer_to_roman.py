def intToRoman(num):
    to_check = {'M':1000, 'CM': 900, 'D': 500, 'CD':400, 'C':100,
                'XC':90, 'L':50, 'XL':40, 'X': 10, 'IX':9, 'V':5, 
                'IV':4, 'I':1,                  
                  }
    roman = []
    remaining_num = num
    
    while remaining_num >0:
        for i,j in to_check.items():
            if remaining_num >= j:
                roman.append(i)
                remaining_num -= j
                break
    return(''.join(roman))
            
            
            
print(intToRoman(1994))