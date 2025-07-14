'''
Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Example 2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
'''
s = "5F3Z-2e-9-ww"
k = 4
# s1 = s.upper()
# print(s1)
def license(s,k):
    s1 = (s.replace('-', '')).upper()
    first_element = (len(s1)%k)
    final_string_list = []
    if first_element:
        final_string_list.append(s1[0:first_element])
    for i in range(first_element,len(s1), k):
        final_string_list.append(s1[i:i+k])
    return ('-'.join(final_string_list))        
        
print(license(s,k))