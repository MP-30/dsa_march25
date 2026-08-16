def for_deco(func):
    def modify(n: int):
        for i in range(n):
            func(i + 5)
    return modify

@for_deco
def new_loop(k):
    print(k)

new_loop(8)