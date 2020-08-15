# Day_19: August/15/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by teclado (Day: 4 {collections})

# Here we have a list containing three tuples, where each tuple contains two items.
imaginary_books = [
    ('30 Days of Python', 2004),
    ('30 Days of Javascript', 2005),
    ('30 Days of Programming', 2007)
]


# defining a tuple with single value:
name = "John",   # The comma must be used for tuple.
# or,
name = ("John",)

imaginary_books = [
    (
        '30 Days of Python', 
        'Abdullah',
        2004
    ),
    (
        '30 Days of Javascript',
        'Asadullah', 
        2005
    ),
    (
        '30 Days of Programming',
        'Amatullah',
        2007
    )
]

print((imaginary_books[0]))          # ('30 Days of Python', 'Abdullah', 2004)
print(type(imaginary_books[0]))      # <class 'tuple'>
print(type(imaginary_books))         # <class 'list'>

print(imaginary_books[0][0])         # 30 Days of Python
print(imaginary_books[1][2])         # 2005

book = imaginary_books[1][0]
print(book)                          # 30 Days of Javascript

books = [
    (
        "Python Crash Course",
        "Eric",
        2005
    )
]
# Another book:
book_title = input("Enter your favourite book's title: ")
author = input("Enter director: ")
year = input("Enter your reading year: ")

new_book = book_title, author, year
print(new_book)
print(type(new_book))                # <class 'tuple'>

# adding this book to the books list:
books.append(new_book)
print(books)

# printing the title and author of the book:
print(f"{new_book[0]} ({new_book[1]})")

del books[0]  # it will delete the first item of the book.