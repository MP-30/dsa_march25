import random

class Employee():

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.emp_id = self.generate_employee_is()
        
    def generate_employee_is(self):
        return f"EMP-{random.randint(100,999)}"

    def get_employee_details(self):
        print(f'Employee details: Age:{self.age}, Id: {self.emp_id}, Name: {self.name}, Position: {self.position}')

    print ('this is employee class')

emp1 = Employee('Aditya', '34', 'Software developer')
emp2 = Employee('Rahul', '24', 'Software developer - 2')
emp3 = Employee('Kumar', '32', 'Software developer - 1')
emp1.get_employee_details()
emp2.get_employee_details()
emp3.get_employee_details()