#Topic: Formatting strings and processing user input & String interpolation:
#Day_2: July/30/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya


print("Nikita is 24 years old.")
print("{} is {} years old".format("John", 24))
print("My name is {}.".format("Alifa"))

output="{} is {} years old, and {} works as a {}."                             #variable
print(output.format("John", 24, "John", "web developer"))

#or,
string_example = "{0} is {1} years old, and {0} works as a {2}."               #1st value will always be 0.
print(string_example.format("Nikita", 24, "web developer"))                    #The values inside .foramt is called placeholder.

#or,
example = "{name} is {age} years old, and  {name} works as an {job}."          #placeholder and variable 
print(example.format(name = "Alex", age = 40, job = "engineer"))

#or,
name= "Jim"
age= 26                                                                        #Concatenation
print(name,"is", age, "years old.")                                            #Output: Jim is 26 years old.

#or,
name= "Karim"
print(name, "is 30 years old.")

#or,
name3= "Amina"
country= "Syria"                                                               #Output: Amina lives in Syria.
print("{} lives in {}.".format(name3, country))                                #variable and string interpolation.

#f-string syntax:
name4 = "Muhammad"
age4 = 30
print(f"{name4} is {age4} years old.")                                         #f-string ব্যবহার করার কারণে আমরা সেকেন্ড ব্র্যাকেটের {curly braces} মধ্যেই যা ইচ্ছা লিখতে পারছি।

#Let's calculate Muhammad's age in months by f- string:
print(f"{name4} is {age4 * 12} months old.")                                   #Output: Muhammad is 360 months old.