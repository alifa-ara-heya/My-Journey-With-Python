# Day_9: August/05/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Asabeneh (30 Days of Python: Day-5 (exercises))

# 1. Declare an empty list
empty_list = []                          # Don't use 'list' as a list or variable name, it is a reserved word.

# 2. Declare a list with more than 5 items:
languages = ['C++', 'C', 'C#', 'Ruby', 'Java', 'SQL', 'Python']

# 3. Find the length of your list
print(len(languages))                    # 7

# 4. Get the first item, the middle item and the last item of the list.
first_item = languages[0]
print(first_item)                        # C++

middle_item = languages[3]
print(middle_item)                       # Ruby

last_item = languages[-1]
print(last_item)                         # Python

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Ayesha", "15", "5.3 ft", "no", "Libya"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
print(it_companies)                                        # ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 8. Print the number of companies in the list.
number_of_companies = len(it_companies)
print("Number of companies:", number_of_companies)         # Number of companies: 7

# 9. Print the first, middle and last company.
first_company = it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]

print(first_company)                      # Facebook                  
print(middle_company)                     # Apple
print(last_company)                       # Amazon

# 10. Print the list after modifying one of the companies.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[-1] = 'Alibaba'
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Alibaba']

# 11. Add an IT company to it_companies.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append('Alibaba')
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Alibaba']

# 12. Insert an IT company in the middle of the companies list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(3, "Alibaba")
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'Alibaba', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[1].upper())            # GOOGLE

# 14. Join the it_companies with a string '#;'
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
joined_it_companies = "#; " .join(it_companies)
print(joined_it_companies)                # Facebook#; Google#; Microsoft#; Apple#; IBM#; Oracle#; Amazon

# 15. Check if a certain company exists in the it_companies list.
check = "Google" in it_companies
print(check)                              # True
check = "Teletalk" in it_companies
print(check)                              # False
#or,
print("Facebook" in it_companies)         # True

# 16. Sort the list using sort() method.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)                       # ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle']

mixed_data_types = ["Ayesha", "15", "5", "5.3 ft", "no", "Libya"]
mixed_data_types.sort()
print(mixed_data_types)                   # ['15', '5', 5.3 ft', 'Ayesha', 'Libya', 'no']

# 17. Reverse the list in descending order using reverse() method.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse = True)
print(it_companies)                       # ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

# 18. Slice out the first 3 companies from the list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three = it_companies[0:3]
print(first_three)                        # ['Facebook', 'Google', 'Microsoft']

# 19. Slice out the last 3 companies from the list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
last_three = it_companies[-3:]
print(last_three)                         # ['IBM', 'Oracle', 'Amazon']

# 20. Slice out the middle IT company or companies from the list.
middle_company = it_companies[-4:-3]
print(middle_company)                     # ['Apple']

# 21. Remove the first IT company from the list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("Facebook")
print(it_companies)                       # ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#or,
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)
print(it_companies)                       # ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#or,
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[0]
print(it_companies)                       # ['Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 22. Remove the middle IT company or companies from the list:
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(3)
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon'] ('Apple' removed)
#or,
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[3:5]
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'Oracle', 'Amazon'] ("Apple", "IBM" removed)

# 23. Remove the last IT company from the list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(-1)
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle']
#or,
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[-1]
print(it_companies)                       # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle']

# 24. Remove all IT companies from the list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[0:7]
print(it_companies)                       # []
#or,
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)                       # []

# 25. Destroy the IT companies list.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies[:]
print(it_companies)                       # []

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)                        # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = joined_list.copy()
print(full_stack)                         # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)                         # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']