def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print("Hello, {name}")
    
# say_hello("Aditya")

def Countdown(n):
    while n> 0:
        yield n
        n -=1
        
for number in Countdown(5):
    print(number)