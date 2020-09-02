t = ('a', 'b', 'c', 'd')
t1 = ('a',)

t2 = tuple()
print(t2)         # ()

t4 = tuple('important')
print(t4)         # ('i', 'm', 'p', 'o', 'r', 't', 'a', 'n', 't')

print(t4[1])      # m
print(t4[1 : 3])  # ('m', 'p')

# You can’t modify the elements of a tuple, but you can replace one tuple with another:

t = ('A',) + t[1:]
print(t)          # ('A', 'b', 'c', 'd')