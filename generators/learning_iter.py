my_list = (1, 2, 3)  # my_list is iterable, not an iterator

# Get an iterator from the list
my_iterator = iter(my_list)

# # Use the iterator
# print(next(my_iterator))  # Output: 1
# print(next(my_iterator))  # Output: 2
# print(next(my_iterator))  # Output: 3

# print(next(my_iterator))  # Raises StopIteration


for i in my_list:
    print(i)