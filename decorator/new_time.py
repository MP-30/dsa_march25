import  time

def time_deco(func):
    def calculate_time(*args):
        t1 = time.time()
        func(*args)
        t2 = time.time()
        print(t2 - t1)
    return calculate_time

@time_deco
def check(n):
    for i in range (0,n):
        j = i

check(700000000)