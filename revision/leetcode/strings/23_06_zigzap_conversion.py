s = "PAYPALISHIRING"

# class Solution:
#     def convert(self, s:str, numRows: int) -> str:
#         ...
        
        
def print_num(numRows,s):
    a = list(range(0,numRows)) + list(range(numRows-2,0,-1))
    while len(a)< len(s):
        a +=a
    print(a[:len(s)])
    new_list = []
    for i in range(0,len(s)):
        new_list.append([a[i],s[i]])
    print(new_list)
    
    new_dict = {}
    for j in new_list:
        if j[0] not in new_dict.keys():
            new_dict[j[0]] = [j[1]]
        elif j[0] in new_dict.keys():
            new_dict[j[0]].append(j[1])
    print(new_dict)
    
    result = []
    for k in new_dict.values():
        result.extend(k)
    print(''.join(result))
    
    
print_num(4,s=s)

u = [[0, 'P'], [1, 'A'], [2, 'Y'], [2, 'P'], [1, 'A'], [0, 'L'], [1, 'I'], [2, 'S'], [2, 'H'], [1, 'I'], [0, 'R'], [1, 'I'], [2, 'N'], [2, 'G']]
v = [0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 1, 2, 2]