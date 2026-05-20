input_list = [0,1,1,1,0,1,1,0,1,1,0]
output = 5
def solve(input_list):
    maxx = 0
    for i in range(len(input_list)):
        if input_list[i] == 0:
                summ = 0
                for j in input_list[i-1::-1]:
                    if j == 1:
                        summ +=1
                    else:
                        break
                for k in input_list[i+1:]:
                    if k == 1:
                        summ +=1
                    else:
                        break
                maxx = max(maxx, summ+1)
    return maxx

print(solve(input_list))
                
