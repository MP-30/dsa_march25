class Person:
    def __init__(self,fname, flast):
        self.fname = fname
        self.flast = flast
        
    def printname (self):
        print(self.fname, self.flast)
        
        
class Student(Person):
    def __init__(self,fname, flast, year):
        super().__init__(fname, flast)
        self.grandfather_age = year
        
    def welcome(self):
        print("welcome", self.fname, self.flast, self.grandfather_age)
c = Student('Mime', 'Kuman', 576)
c.welcome()