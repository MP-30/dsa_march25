def chuchu(widths, s):
    per_line = 0
    line_count = 1
    for i in s:
        value = ord(i) - ord('a')
        a= per_line + widths[value]
        if a <= 100:
            per_line = a
            continue
        elif a >100:
            per_line =0
            per_line += widths[value]
            line_count+=1
    result = [line_count, per_line]
    return result
            
    ...
    
    
# widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# s = "abcdefghijklmnopqrstuvwxyz"

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"

print(chuchu(widths, s))
