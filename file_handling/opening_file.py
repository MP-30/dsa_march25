file = open("file_handling/hello.txt","r")
if file:
    print(file.read())
    print(type(file))
file.close()

# age = input('Enter your age: ')
# f = open("file_handling/age.txt",'w')
# f.write(age)
# f.close()