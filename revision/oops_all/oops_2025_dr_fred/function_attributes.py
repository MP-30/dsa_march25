# class Person:
#     def say_hello(*args):
#         print('Hello',args)

# print(Person.say_hello)
# print(type(Person.say_hello))

# print(Person.say_hello())

# # p.say_hello()

# class Person: 
#     def set_name(instance_obj, new_name):
#         instance_obj.name = new_name
        
# p = Person()
# print(p.set_name('Aditya'))

# print(p.__dict__)
# Person.set_name(p,'Singh')
# print(p.__dict__)


class Person: 
    def say_hello(self):
        print(f'{self} says hello')
        
p = Person()
print(p.say_hello)        
print(Person.say_hello)

m_hello = p.say_hello
print(m_hello)
print(m_hello.__func__)

Person.do_work = lambda self: f"do_work called form {self}"
print(Person.__dict__)