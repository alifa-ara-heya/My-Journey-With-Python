# Asabeneh  30 daysofpython

# one way
lang = 'Python'
lst = list(lang)
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']


# second way
lst = [i for i in lang]
print(type(lst))
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']


# For instance if you want to generate a list of numbers.
numbers = [i for i in range(11)]
print(numbers)   #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [i * i for i in range(11)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples.
t_nums = [(i, i* i) for i in range(11)]
print(t_nums)    # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]


even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)     # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
print_positive_even = [i for i in numbers if i % 2 == 0 and i > 0]
print(print_positive_even)    # [4, 6, 8, 10]


# Flattening a three dimensional array:
three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in three_dimen_list for number in row]
print(flattened_list)         # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Exercises:
# Filter only negative and zero in the list using list comprehension.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero = [i for i in numbers if i <= 0]
print(negative_zero)          # [-4, -3, -2, -1, 0]


# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [4, 5, 6]], [[7, 8, 9]]
#flat_list = [i for row in ]

