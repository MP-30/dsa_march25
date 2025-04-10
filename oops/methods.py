class Elephant():
    def eat(self):
        print("I am eatting")


class Human(Elephant):
    def speak(self):
        print('speak')



class ParentClass(Human, Elephant):
    """This is main class which is holding all logic of methods"""

    def __new__(cls, *args, **kwargs):
        print('In dundder __new__')
        return super().__new__(cls)

    def __init__(self, name , age):
        print('this is __init__')
        self.name = name 
        self.age = int(age)

    def show_details(self):
        print(self.name, self.age)

    def increment_details(self):
        self.age +=1

emp1 = ParentClass('Aditya', '30')
emp1.increment_details()
emp1.show_details()