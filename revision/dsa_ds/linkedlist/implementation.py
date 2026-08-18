import copy

a = 4
b = copy.deepcopy(a)

print(b)


class variable:
    a = 8
    
constrotar = variable()
b = constrotar.a
print(b)