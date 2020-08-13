# Day_17: August/13/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 7 {sets})


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies.
print(len(it_companies))            # 7

# 2. Add 'Twitter' to it_companies.
it_companies.add('Twitter')
print(it_companies)                 # {'IBM', 'Microsoft', 'Oracle', 'Google', 'Amazon', 'Twitter', 'Facebook', 'Apple'}

# 3. Insert multiple IT companies at once to the set it_companies.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.update(["Twitter", "Alibaba", 'Aliexpress'])
print(it_companies)                 # {'Google', 'Facebook', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Microsoft', 'Aliexpress', 'Alibaba', 'Twitter'}

# 4. Remove one of the companies from the set it_companies.
it_companies.remove("Aliexpress")
print(it_companies)                 # {'Apple', 'Twitter', 'Google', 'Microsoft', 'Oracle', 'Alibaba', 'Facebook', 'Amazon', 'IBM'}

# 5. What is the difference between remove and discard.
# Ans: We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
it_companies.discard("Robi")
print(it_companies)               # no traceback.

#6. Join A and B:
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print(A)                          # {19, 20, 22, 24, 25, 26, 27, 28}

# 7. Find A intersection B.
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))          # {19, 20, 22, 24, 25, 26}

# 8. Is A subset of B.
print(A.issubset(B))              # True

# 9. Are A and B disjoint sets.
print(A.isdisjoint(B))            # False

# 10. Join A with B and B with A.
A.update(B)
print(A)                          # {19, 20, 22, 24, 25, 26, 27, 28}
B.update(A)
print(B)                          # {19, 20, 22, 24, 25, 26, 27, 28}

# 11. What is the symmetric difference between A and B.
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.symmetric_difference(B))  # {27, 28}

# 12. Delete the sets completely.
del A
del B

# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print(ages)                     # {19, 22, 24, 25, 26}
print(len(age) - len(ages))     # 3
print(len(age) > len(ages))     # True (list is bigger)

# 14. Explain the difference between the following data types: string, list, tuple and set.

# 15. "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.
sentence = "I am a teacher and I love to inspire and teach people."
print(sentence.split())        # ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.']
print(type(sentence))          # <class 'str'>
sentence = set(sentence)
print(sentence)