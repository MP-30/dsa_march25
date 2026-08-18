my_list = (1, 2, 3)  # my_list is iterable, not an iterator

# Get an iterator from the list
my_iterator = iter(my_list)

# # Use the iterator
# print(next(my_iterator))  # Output: 1
# print(next(my_iterator))  # Output: 2
# print(next(my_iterator))  # Output: 3

# print(next(my_iterator))  # Raises StopIteration

my_iterator1 = iter(my_list)
print(next(my_iterator1))
print(next(my_iterator1))
print(next(my_iterator1))