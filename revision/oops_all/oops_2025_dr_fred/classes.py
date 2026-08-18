class MyClass():
    language = 'Python'
    version = '3.6'
    

my_obj = MyClass()
print(setattr(MyClass, 'language', 'Java'))    
print(MyClass.language)
print(my_obj.version)
print(getattr(MyClass, 'languae', 'None'))
print(setattr(MyClass, 'language', 'Java'))
setattr(MyClass, 'languages', 'C++')
print(MyClass.languages)
del MyClass.languages
print(MyClass.__dict__)