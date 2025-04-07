# def greet_decorator(func):
#     def wrapper(name):
#         print("Getting ready to greet...")
#         func(name)
#         print("Done greeting!")
#     return wrapper

def test_deco(func):
    def check(name):
        print(f"Hello i am {name} 56")
    return check

@test_deco
# @greet_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Aditya")
