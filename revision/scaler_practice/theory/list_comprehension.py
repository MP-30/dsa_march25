# result = []
# for i in range(1,6):
#     result.append(i**2)
# print(result)

# list comprehension
# result = [x**2 for x in range(0,6)]
# print(result)

result = [x**2 for x in range(0,6) if x >2]
print(result)