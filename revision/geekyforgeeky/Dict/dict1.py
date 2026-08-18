import time
def docorator_function(func):
    def main_function(*args, **kwargs):
        start_time = time.time()
        # print(f'this is deco func {name}')
        func(*args, **kwargs)
        end_time = time.time()
        print(abs(start_time - end_time))
    return main_function



# Extract Unique values dictionary values


test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}

def find_unique(test_dict):
    new_list = []
    for i,j in test_dict.items():
        for k in j:
            new_list.append(k)
    print(set(new_list))




# Find the sum of all items in a dictionary

d1 = {'a': 100, 'b': 200, 'c': 300}

def sum_of_values(d1):
    final_sum = 0
    for i in d1.values():
        final_sum += i
    print(final_sum)

# Ways to remove a key from dictionary

d2 = {"name": "Nikki", "age": 25, "city": "New York", "height": 7, 'food': 'milk', 'country': 'india', 'hobby': 'cricket'}

def remove_key(d2):
    d2.pop('name')
    del d2['age']
    d2.popitem()
    d2.pop ('city', 'New York')
    print(d2)


# Ways to sort list of dictionaries by values Using itemgetter

from operator import itemgetter

data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19},
             {"name": "Nikhili", "age": 39}]
@docorator_function
def ways_to_sort(data_list):
    print(sorted(data_list, key=itemgetter('name')))

def ways_to_sort_inbuild():
    pass

# Ways to sort list of dictionaries by values Using lambda function

@docorator_function
def ways_to_sort_lambda(data_list):
    print(sorted(data_list, key=lambda i:i['age']))



# Merging two Dictionaries

dict_1 = {'aditya': 34, 'rahul':12}
dict_2 = {'vivek': 13, 'ravi': 45}

def merge_two_dict(dict_1, dict_2):
    print(dict_1 )

# Convert key-values list to flat dictionary
a2 = [("name", "Alice"), ("age", 25), ("city", "New York")]

def convert_list_dic(a2):
    new_dict = {}
    for i in a2:
        new_dict[i[0]] = i[1]
    print(new_dict)

# Insertion at the beginning in OrderedDict

from collections import OrderedDict

def insert_at_beg():
    new_dict = OrderedDict([('aditya',12), ('singh',3)])
    new_dict = OrderedDict([('rahul',8)] + list(new_dict.items()))
    print(new_dict)


# Check order of character in string using OrderedDict( )

# not doing this


# Dictionary and counter to find winner of election

from collections import Counter

votes =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']

def count_votes(votes):
    vote_count = {}
    for i in votes:
        if i not in vote_count:
            vote_count[i] = 1
        elif i in vote_count:
            vote_count[i] +=1
    max_vote = 0
    winner = 0
    for j,k in vote_count.items():
        if k > max_vote:
            max_vote = k
            winner = j
    print(max_vote, winner)


# Append Dictionary Keys and Values ( In order ) in dictionary
keys1 = ["name", "age", "city"]
values1 = ["Alice", 30, "New York"]
def append_dict(keys1, values1):
    print(dict(zip(keys1, values1)))

# Sort Python Dictionaries by Key or Value

def sort_dict(data_list):
    print(sorted(data_list, key=itemgetter('name')))


# Sort Dictionary key and values List

'''
Input : test_dict = {'c': [3], 'b': [12, 10], 'a': [19, 4]} 
Output : {'a': [4, 19], 'b': [10, 12], 'c': [3]} 

Input : test_dict = {'c': [10, 34, 3]} 
Output : {'c': [3, 10, 34]}
'''

Input1 = {'c': [10, 34, 3]} 
Input2 = {'c': [3], 'b': [12, 10], 'a': [19, 4]} 

def sort_dict1(intp):
    new_dict = {}
    for i in sorted(intp):
        new_dict[i] = sorted(intp[i])
    print(new_dict)


# Handling missing keys in Python dictionaries

country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}

def handling_missing(country_code):
    print(country_code.get('India', 'Not found'))

# Dictionary with keys having multiple inputs

def having_multi_input():
    dict = {}
    x, y, z = 10, 20, 30
    dict[x, y, z] = x + y - z
    print(dict)

# 

@docorator_function
def test_func(i):
    for j in range(0,i):
        print(j)
    
if __name__ == '__main__':
    # find_unique(test_dict)
    # sum_of_values(d1)
    # remove_key(d2)
    # ways_to_sort_inbuild(data_list)
    # ways_to_sort(data_list)
    # ways_to_sort_lambda(data_list)
    # test_func(5)
    # convert_list_dic(a2)
    # insert_at_beg()
    # count_votes(votes)
    # append_dict(keys1, values1)
    # sort_dict(data_list)
    # sort_dict1(Input2)
    # handling_missing(country_code)
    having_multi_input()
    pass