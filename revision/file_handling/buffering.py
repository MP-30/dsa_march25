f1 = open('file_handling/hello.txt', mode='r', buffering=10, encoding='UTF-8')
if f1:
    print("opened")
    print(f1)