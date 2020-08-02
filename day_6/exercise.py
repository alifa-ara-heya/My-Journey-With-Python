#Calculating the area of a triangle:
base = input("Enter base: ")
height = input("Enter height: ")
area_of_the_triangle = 0.5 * float(base) * float(height)
print(f"The area of the triangle is: {area_of_the_triangle}square unit.")
print("---------")


#Calculating the perimeter of triangle:
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perimeter = float(side_a) + float(side_b) + float(side_c)
print(f"The perimeter of the triangle is: {perimeter} unit.")
print("---------")

#Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point(6,10), or,
#Calculating the slope between two points (2, 2) and (6, 10):
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
print("slope is", slope)


#Checking if a number is even or odd:
x = input("Enter a number: ")
if int(x) % 2 == 0:
    print("Even number")
else:
    print("Odd number")