import time
def find_time(func):
    def wrapper(*args, **kwargs):
        a = time.time()
        result = func(*args, **kwargs)
        b = time.time()
        execution_time = abs(a-b)
        print(f"'{func.__name__}' ran in: {execution_time:.4f} seconds")
        return result
    return wrapper

@find_time
def helll():
    print('hello')
    
helll()