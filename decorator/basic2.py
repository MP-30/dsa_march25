def deco (func):
    def to_check_its_working():
        print('This is for testing purpose')
        func()
    return to_check_its_working

@deco
def this_is_normal_function():
    print('normal funciton')


# this_is_normal_function()

import time

def deco2(func):
    def checking_func(*args, **kwargs):
        print('this is deco')
        start_time = time.time()
        result =  func(*args, **kwargs)
        end_time = time.time()
        print(f'time taken  {end_time - start_time}')
        return (result)
    return checking_func

@deco2
def for_loop():
    res = 0
    for i in range(1,6):
        res += i
    print(res)
    
    
if __name__ == '__main__':
    for_loop()
    