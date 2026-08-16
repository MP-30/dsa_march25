def modify_loop(func):
    def modify_func(n):
        func ( n + 5)
    return modify_func

@modify_loop
def print_something(k):
    print(k)

print_something(8)