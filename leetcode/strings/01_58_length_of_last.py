s = "Hello World"
def length(s):
    start_index = -1
    end_index = -1
    i = -1
    while s[i] ==' ':
        i = i -1
        start_index = i
    j = start_index
    while s[j] != ' ':
        end_index = j
        j = j -1    
    final_start_index = 0
    if start_index == -1:
        final_start_index = None
    else: final_start_index = start_index
    
    return(s[end_index:final_start_index])
        
length(s)
# print(s[-5:-1])