# Day_8: August/04/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
#From: Asabeneh (30 Days of Python: Day-5)

# List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
# A list can be empty or it may have different data type items or items

# syntax (using list built-in function)
lists = list()

empty_list = list()                          # an empty list
print(len(empty_list))                       # 0

# syntax (using square brackets)
lists = []
empty_list = []                              # this is an empty list
print(len(empty_list))                       # 0

fruits = ['banana', 'orange', 'mango', 'lemon', 'carrot']
fruits2 = list('banana' 'orange' 'mango' 'lemon' 'carrot')
fruits3 = list('banana orange mango lemon carrot')
print(fruits)                                # ['banana', 'orange', 'mango', 'lemon', 'carrot']
print(fruits2)                               # ['b', 'a', 'n', 'a', 'n', 'a', 'o', 'r', 'a', 'n', 'g', 'e', 'm', 'a', 'n', 'g', 'o', 'l', 'e', 'm', 'o', 'n', 'c', 'a', 'r', 'r', 'o', 't']
print(fruits3)
print(type(fruits))                          # <class 'list'>
print(type(fruits2))                         # <class 'list'>

#lists:
vegetables = ['onion', 'Tomato', 'carrot', 'brocoli']
animal_products = ['milk', 'meat', 'butter', 'cheese', 'yogurt', 'icecream']
web_tec = ['HTML', 'CSS', 'JavaScript', 'React','Redux', 'Node', 'MongoDB']
countries = ['Bangladesh', 'Syria', 'Iraq', 'Libya', 'Afghanistan']


# Print the lists and its lengths:
print('Fruits:', len(fruits))                              # Fruits: 5
print('Vegetables I love:', len(vegetables))               # Vegetables I love: 4
print("Number of Web Technologies:", len(web_tec))         # Number of Web Technologies: 7
print("Countries I adore:", len(countries))                # Countries I adore: 5


#Lists can have different data types:
example_list = ['Fatima', 150, True, {'country':'Bangladesh', 'city':'Sylhet'}, {'Red','Blue','Black'}]
print(example_list)


# Accessing list items using positive index. A list index starts from 0.
fruits = ['banana', 'orange', 'mango', 'lemon', 'carrot']
#index:       0        1        2        3         4

first_fruit = fruits[0]
print(first_fruit)                # banana
last_fruit = fruits [4]
print(last_fruit)                 # carrot


# Accessing list items using negative index.
fruits = ['banana', 'orange', 'mango', 'lemon', 'carrot']
#index:       -5       -4       -3       -2        -1

first_fruit = fruits [-5]
print(first_fruit)                # banana
second_last = fruits [-2]
print(second_last)                # lemon


# Unpacking list items:
# Example-1:
list1 = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = list1
print(first_item)                 # item1
print(second_item)                # item2
print(third_item)                 # item3
print(rest)                       # ['item4', 'item5']

# Example-2:
fruits = ['banana', 'orange', 'mango', 'lemon', 'carrot','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)                # banana
print(second_fruit)               # orange
print(third_fruit)                # mango
print(rest)                       # ['lemon', 'carrot', 'apple]

# Example-3:
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)                      # 1
print(second)                     # 2
print(third)                      # 3
print(rest)                       # [4, 5, 6, 7, 8, 9]
print(tenth)                      # 10

# Example-3:
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)                         # Germany
print(fr)                         # France
print(bg)                         # Belgium
print(sw)                         # Sweden
print(scandic)                    # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)                         # Estonia

# Example-4:
cities = ['Dhaka', "Chittagong", 'Barishal', "Khulna", "Sylhet", "Jessore", "Rajshahi","Bogra"]
Dha, Ctg, Bar, Khu, *two_cities, raj, bog = cities
print(Dha)                        # Dhaka
print(Ctg)                        # Chittagong
print(Bar)                        # Barishal
print(Khu)                        # Khulna
print(two_cities)                 # ['Sylhet', 'Jessore']
print(raj)                        # Rajshahi
print(bog)                        # Bogra

# slicing items from a list:
# Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list.
# [start: end: stop] = (default values for start = 0, end = len(list)-1 (last item), step = 1)

fruits = ['banana', 'orange', 'mango', 'lemon']
# index:     0          1         2       3 
all_fruits = fruits [0 : 4]
print(all_fruits)                 # ['banana', 'orange', 'mango', 'lemon']
#or,
all_fruits = fruits[0 : ]         # if we don't set where to stop it takes all the rest
print(all_fruits)                 # ['banana', 'orange', 'mango', 'lemon']

orange_and_mango = fruits[1 : 3]
print(orange_and_mango)           # ['orange', 'mango']

orange_mango_lemon = fruits[1 : 4]
print(orange_mango_lemon)         # ['orange', 'mango', 'lemon']

orange_and_lemon = fruits[1:4:2]
print(orange_and_lemon)           # ['orange', 'lemon']

banana_nd_lemon = fruits[0 : 4: 3]
print(banana_nd_lemon)            # ['banana', 'lemon']

orange = fruits[1 : 4: 3]
print(orange)                     # ['orange']

banana_and_mango = fruits[::2]
print(banana_and_mango)           # ['banana', 'mango']   here we used a 3rd argument, step. It will take every 2cnd item - ['orange', 'lemon']


# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]          # returns all the fruits
print(all_fruits)                 # ['banana', 'orange', 'mango', 'lemon']

orange_and_mango = fruits[-3 : -1]
print(orange_and_mango)           # ['orange', 'mango']

orange_mango_lemon = fruits[-3 : ]
print(orange_mango_lemon)         # ['orange', 'mango', 'lemon']

reverse_fruits = fruits[::-1]
print(reverse_fruits)             # ['lemon', 'mango', 'orange', 'banana']   a negative step will take the list in reverse order
# or,
fruits.reverse()
print(fruits)                     # ['lemon', 'mango', 'orange', 'banana']