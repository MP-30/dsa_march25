# class Dog:
#     species = 'Dog'


#     @classmethod
#     def change_species(cls, new_species):
#         cls.species = new_species

# Dog.change_species('indian sheperd')
# print(Dog.species)

"""

class Date_formater:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        print(self.day, self.month, self.year)

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, data_str.split('/'))
        return (day, month, year)

# data_str = "04/03/2023"
data_str = [1,2,2024]

if type(data_str) == str:
    d = Date_formater.from_string(date_str=data_str)
    print(d)
else :
    d = Date_formater(data_str[0], data_str[1], data_str[2])
    print(f'from else condition {d}')

"""


"""

class Math:
    def sun(self,a,b):
        print(a-b)

    @staticmethod
    def add(a,b):
        print(a+b)

math = Math()
math.sun(2,3)

print(Math.add(1,2))

"""



class Product:
    tax_rate = 15
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def final_price(self):
        return self.price * (1 + Product.tax_rate)

    @classmethod
    def change_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate


p = Product(name='cap', price=78)
print(p.final_price())