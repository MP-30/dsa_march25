class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.height = None
    
    def myfunc(self):
        return("Helo This is my name " + self.name )
    
    def __str__(self):
        name = getattr(self, 'name', 'None')
        age = getattr(self, 'age', 'None')
        height = getattr(self, 'height', 'None')
        return (f"{name} and {age} and height is {height}")
    
p1 = Person("adyyy",9)
p1.age = 90
setattr (p1, 'age',80)
print(p1.myfunc())
print(p1.age)

print(p1)