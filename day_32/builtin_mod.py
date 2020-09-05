from statistics import *    # importing all the statistics modules
ages = [20,20,24,24,25,22,26,20,23,22,26]
print(mean(ages))      # 22.90909090909091
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # 2.3001976199685736

import math
print(math.pi)          # 3.141592653589793
print(math.sqrt(2))     # 1.4142135623730951
print(math.pow(2, 3))   # 8.0
print(math.floor(9.81)) # 9, rounding to the lowest
print(math.ceil(9.81))  # 10, rounding to the highest
print(math.log10(100))  # 2.0, logarithm with 10 as base

#help(math)  # run on the python terminal
#dir(math)   # ru on python terminal (output: ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc'])


#  If we want to import only a specific function from the module we import it as follows:
from math import pi
print(pi)            # 3.141592653589793


# When we import we can also rename the name of the function.
from math import pi as PI
print(PI)              # 3.141592653589793


# string module
import string
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.digits)         # 0123456789

print(string.punctuation)    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random, randint

print(random())      # it doesn't take any arguments; it returns a value between 0 and 0.9999

print(randint(5, 20)) # # it returns a random integer number between 5 and 20