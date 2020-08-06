#Day_6: August/02/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya

#calculating area of a circle:
radius = 30
pi = 3.14
area_of_a_circle = pi * radius ** 2
circumference_of_a_circle = 2 * pi * radius

print("Area of a circle: ", area_of_a_circle, "square meter.")
print("Circumference of the circle is:", circumference_of_a_circle, "meter.")

radius = input('Enter the radius: ')
area_of_a_circle = pi * int(radius) ** 2
print("---------")


#Calculating area of a rectangle:
length = 10
width = 20
area_of_a_rectangle = length * width
perimeter = 2*(length + width)
print("Area of a rectangle:", area_of_a_rectangle)
print(f"Perimeter of the triangle is: {perimeter} unit.")
print("---------")


#Calculating weight of an object:
mass = 75
gravity = 9.81
weight = mass * gravity
print("Weight of an object:", weight, 'N')
#or,
print(f"Weight of an object: {weight}N")
print("---------")


#topic: ask a user their weight (in pounds), convert it to kilograms and print on the terminal.
weight_in_pounds = int(input("Your weight (lbs): "))
weight_in_kg = weight_in_pounds * 0.454
print("Your weight in kg is:", weight_in_kg)
print("---------")