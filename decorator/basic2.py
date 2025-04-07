def deco (func):
    def to_check_its_working():
        print('This is for testing purpose')
        func()
    return to_check_its_working

@deco
def this_is_normal_function():
    print('normal funciton')


this_is_normal_function()