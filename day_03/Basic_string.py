#Day_2: July/30/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya

#Basic string processing:
print("Hello, World!".lower())                                                  #Output: hello, world!
print("Assalamu Alaikum!" .upper())                                             #Output: ASSALAMU ALAIKUM!
print("How are you?" .capitalize())                                             #Output: How are you? (Capitalizes the first character)
print("I am Muslim." .title())                                                  #Output: I Am A Muslim. (Capitalizes the first character of every word.)
print("  Hello, Bangladesh! " .strip())                                         #Output: Hello Bangladesh! (Removes spaces from both ends.)


#How do we print quotation mark / apostrophe?
print("\"I love my ammu.\"")                                                    #Output: "I love my ammu."

#printing multiple lines with line break:
print('''Rain Rain Rain 
Pain Pain Pain
No No No
Go Go Go
I love Rain!''')                                                                #We can use either three single quotation or three double quotation at both ends


#Some exercises:
#exercise_1: Printing a string in different way: "Assalamu Alaikum everybody"
greeting = "Assalamu Alaikum"
print(greeting, "everybody!")
#or,
print("{} everybody!" .format(greeting))
#or,
print("{} everybody!" .format("Assalamu Alaikum"))
#or,
print(f"{greeting} everybody!")                                                  #better

print(f"{greeting} everybody!" .upper())
print(f"{greeting} everybody!" .capitalize())
print(greeting + "!")


#concatenating of string and string:
print("I am" + " 29")
#or, #concatenating of string and integer:
print("I am "+ str(29))

#concatenating of string and string:
print("I am" + " ALifa")

#String interpolation
title = "I am Lion"
Director = "Mali"
release_year= 1950

print("{0} ({1}), directed by {2}" .format(title, release_year, Director))
#or,
print(f"{title} ({release_year}), directed by {Director}")
#or,
print(f"\"{title}\" ({release_year}), directed by {Director}")