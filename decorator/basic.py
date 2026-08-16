# def greet_decorator(func):
#     def wrapper(name):
#         print("Getting ready to greet...")
#         func(name)
#         print("Done greeting!")
#     return wrapper
#
# def test_deco(func):
#     def check(name):
#         print(f"Hello i am {name} 56")
#     return check
#
# @test_deco
# # @greet_decorator
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Aditya")

def new_deco(func):
    def check(name):
        print(f"Helo i am hero {name}")
        func(name)
        return "this is child "
    return check

@new_deco
def hello(name):
    print(f"this is hello from {name}")

print(hello('aditya'))
