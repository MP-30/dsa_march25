import random

class Employee():
    """This is main class which is holding all logic of methods"""

    company_name = 'Google'

    def __new__(cls, *args, **kwargs):
        print('In dundder __new__')
        return super().__new__(cls)

    def __init__(self, name, age, designation):
        print('this is __init__')
        self.name = name
        self.designation = designation 
        self.age = int(age)

    def get_employee_details(self):
        print(self.name, self.age, self.designation, self.company_name)

    def increment_details(self):
        self.age +=1

# this is class method
    @classmethod
    def change_company_name(cls):
        companies = ['Reliance', 'Google', 'Yahoo!', 'Apple']
        company =  random.choice(companies)
        cls.company_name = company
        print('Company changed')

    @classmethod

    def get_class_variables(cls):
        print('Class variables')


Employee.change_company_name()
Employee.get_class_variables()


emp1 = Employee('Aditya', '30','Software Engineer')
emp1.company_name = 'Yohoo!'
emp1.increment_details()
emp1.get_employee_details()


emp2 = Employee('Vivek', '40','Software Engineer 2')
emp2.increment_details()
emp2.get_employee_details()


emp3 = Employee('Rohit', '35','Software Engineer 2')
emp3.increment_details()
emp3.get_employee_details()