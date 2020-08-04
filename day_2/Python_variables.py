#Day_2: July/29/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya

Name = "Alifa Ara Heya"
Year = 2020
Country = "Bangladesh"
Identity = "Muslim"

print(Name)
print(Country)
print(Year)
print(Identity)
print("My name is", Name)

#Calculating and printing the number of days, weeks, and months in 27 years:
days_in_27_years = 365 * 27
months_in_27_years = 12 * 27
weeks_in_27_years = (365 / 7) * 27

print("Days in 27 years: " , days_in_27_years)           # Here we can't use plus to concatenate because our variable is integer. String and integer can't be concatenated.
print("Months in 27 years: ", months_in_27_years)
print("Weeks in 27 years: ", int(weeks_in_27_years))


#Calculating and printing the area of a circle with a radius of 5 units:
pi= 3.1417
radius= 5

print("Area of a circle:", pi * radius ** 2)
#or we can use the pow() function to do this exactly:
print("Area of a circle:", pi * pow(radius,2))



#declaring some more variables:
skills= ['hTML', 'CSS', 'Python']
person_info = {
    'firstname' : 'Alifa',
    'lastname' : 'Hiya',
    'country' : 'Bangladesh',
    'city' : 'Dhaka'
}
print(type(person_info))
print(skills)
print(person_info)

#type casting:
#str to list:
firstname = 'Alifa'
print("First Name:", list(firstname))        # output: ['A', 'l', 'i', 'f', 'a']
#or,
firstname = list(firstname)
print("First name in list:", firstname)


# Declaring variables in one line:
name, country, city, age = "Fatema", "Bangladesh", "Rajshahi", 25
print(name)                                  # Fatema
print(country)                               # Bangladesh
print(city)                                  # Rajshahi
print(age)                                   # 25