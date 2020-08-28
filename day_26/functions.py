# 27 - Aug - 2020
# 30 Days of Python by Asabeneh (day 11)
# Functions

# function without parameters:

def generate_full_name():
    first_name = 'Amatullah'
    last_name = 'Khadeeja'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()                      # Amatullah Khadeeja
# print_full_name = generate_full_name()  # Amatullah Khadeeja
# print(print_full_name)                    # None
print(generate_full_name())               # Amatullah Khadeeja  (None)


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)                         

add_two_numbers()                         # 5
print(add_two_numbers())                  # 5 none

# return: Function can also return values, if a function does not return any, the value of the function is None.
def generate_full_name2():
    first_name = 'Maryam'
    last_name = 'Ayesha'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name2())              # Maryam Ayesha
generate_full_name2()                     # no output


def add_two_numbers2():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers2())                # 5


# Function with parameters:
def greetings(name):
    message = name + ', welcome to python for everyone!'
    return message

print(greetings('Fatima'))               # Fatima, welcome to python for everyone!


def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(5))                        # 15


def square_number(x):
    return x * x

print(square_number(3))                  # 9


def area_of_a_circle(r):
    Pi = 3.14
    area = f"{Pi * 3.14 ** 2:.3f}"
    return area

print(area_of_a_circle(10))             # 30.959


def sum_of_numbers (n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)

sum_of_numbers(10)                      # 55
sum_of_numbers(100)                     # 5050

# or,
def sum_of_numbers2 (n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers2(100))             # 5050


# two parameter:
def generate_full_name3 (first_name, last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name
print(f"Full name: {generate_full_name3('Alifa Ara', 'Heya')}")   # Full name: Alifa Ara Heya


def sum_two_numbers (num_one, num_two):
    total = num_one + num_two
    return total
print(sum_two_numbers(2, 3))        # 5


def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print(calculate_age(2020, 1950))    # 70


def weight_of_object (mass, gravity):
    weight = f"{mass * gravity:.3f}N"
    return weight
print(weight_of_object(3, 9.8))     # 29.400N


# Passing arguments with key and value:
def print_fullname(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname
print_fullname(firstname = 'Amatullah', lastname = 'Ayesha')  # no output
print(print_fullname(lastname = 'Ayesha', firstname = 'Amatullah'))  # Amatullah Ayesha     (order doesn't matter here.)


def add_two_numbers5(num1, num2):
    total = num1 + num2
    return (total)
print(add_two_numbers5(num2 = 4, num1 = 8))   # 12


# Returning a boolean: Example:
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True   # return stops further execution of the function, similar to break
    return False 

print(is_even(3))     # False
print(is_even(28))    # even  True


# Returning a list: Example:
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 ==0:
            evens.append(i)
    return evens

print(find_even_numbers(10))       # [0, 2, 4, 6, 8, 10]


# Function with Default Parameters:
def greetings2 (name = 'Peter'):
    message =  f"{name}, welcome to python for everybody!"
    return message
print(greetings2())                # Peter, welcome to python for everybody!
print(greetings2('Ayesha'))        # Ayesha, welcome to python for everybody!


def weight_of_object2 (mass, gravity = 9.8):
    weight = f"{mass * gravity}N"
    return weight    
print(weight_of_object2(2))        # 19.6N
print(weight_of_object2(2, 9.8))   # 19.6N


# Arbitrary Number of Arguments: If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total
print(sum_all_nums(5, 10, 20))     # 35


# Default and Arbitrary Number of Parameters in Functions.
def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
    
generate_groups('Team-1', 'Ayesha', 'Fatima', 'Maryam')   # Team-1 Ayesha Fatima Maryam


# Function as a Parameter of Another Function:
def square_number2 (n):
    return n * n
def do_something (f, x):
    return f(x)

print(do_something(square_number2, 3))     # 9