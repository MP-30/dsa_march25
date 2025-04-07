# def to_check(a,b):
#     yield a
#     yield b

# result =to_check(10,20)
# # new1 = list(result)
# # print(new1)
# # print(type(new1))

# print(next(result))
# print(next(result))


def new_sh(a,b):
    while a <=b:
        yield a
        a +=1


result = new_sh(1,5 )

print (next(result))

for i in result:
    print(i)