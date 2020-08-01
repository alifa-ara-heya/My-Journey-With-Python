#Day_4: July/31/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya

#Book: Python Crash Course by Eric Matthes
#Topic: Some more on strings and numbers:

example = "This is a string"

example = "This is also a sting."

print(example)

print('1. I told my friend, "Python is my favourite language!"')
#or,
print('2. I told my friend, \"Python is my favourite language!\"')                        #same output

print('3. The language "Python" is named after Monty Python, not the snake.')

name = "ada lovelace"
print("4.", name.title())
print("5.", name.upper())
print("6.", name.lower())
print("7.", name.capitalize())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
#or,
print(full_name.title())
#or,
print(f"10. {first_name} {last_name}")
print(f"{first_name} {last_name}" .upper())
#or,
print("{} {}" .format(first_name, last_name))
#or,
print("{} {}" .format(first_name, last_name) .title())


#adding whitespace to strings with Tabs or Newlines:
print("Python")
print("\tPython")                                                #Adds a tab on output.
print("Languages:\n\tPython\n\tC\n\tJavascript")                 #\n = new line          \t = tab

#removing whitespaces:
fav_lang = 'Python '
print(fav_lang+"2")
fav_lang = fav_lang.rstrip()                                     #.rstrip() removes the end space and we assigned a new value to fav_lang.
print(fav_lang+"2")

fav_lang = ' html'
print("2" + fav_lang)
fav_lang = fav_lang.lstrip()                                     #.lstrip() removes the front space.
print("2" + fav_lang)

fav_lang = ' JavaScript '
print("2" + fav_lang + "3")

fav_lang = fav_lang.strip()                                      #.strip() removes all whitespaces before and after the argument. 
print("2" + fav_lang + "3")


#numbers:
print(0.2 + 0.1)

universe_age = 14_000_000_000                                     #Python ignores underscores in mathematical operation.
print(universe_age)

x , y, z = 1, 2, 3                                                #assigning multiple variables in a single line.
print(x)
print(y)
print(z)


#A message:
name = input("Enter your name: ")
name = name.title().strip()
message = f"Hello {name}, do you want to learn some Python today?"
print(message)