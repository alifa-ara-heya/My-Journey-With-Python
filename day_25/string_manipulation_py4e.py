# Day- 25
# Aug - 26- 2020
# Python 4 everybody (chapter - 6)

# traversal

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1              # b  a  n  a  n  a
    

print(fruit[:])             # banana

# immutable string

greeting = 'Hello, vs code!'
new_greeting = 'J' + greeting[1 :]
print(new_greeting)         # Jello, vs code!


# The following program counts the number of times the letter “a” appears in a string:
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)                # 3

# a more efficient way to do this:
word = 'banana'
print(word.count('a'))      # 3

# if you want to see which methods are available for a data type, use dir.
print(dir(word))

# if you want to see what work a method does type help like the following.
help(str.capitalize)

# slicing: slicing (uct.ac.za) from the following string.
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
at = data.find('@')
print(at)        # 21
space = data.find(" ", at)
print(space)     # 31
print(data[at + 1 : space])       # uct.ac.za

# formatting:
camels = 42
print('%d' % camels)              # 42
print("I have spotted %d camels." %camels)   # I have spotted 42 camels.

print("In %d years I have spotted %g %s." %(3, 0.1, 'camels'))  # In 3 years I have spotted 0.1 camels.

# %d = integer
# %g = float
# %s = string


# Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

text = "X-DSPAM-Confidence:    0.8475"
a = text.find('0')
print(float(text[a : ]))      # 0.8475