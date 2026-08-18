import time

def time_deco(func):
    def check(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execute_time = abs(start_time-end_time)
        print(execute_time)
        return result
    return check

@time_deco
def hello_time():
    for i in range(100000000):
        j = i *i
        
hello_time()