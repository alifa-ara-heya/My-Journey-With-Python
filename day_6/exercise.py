#Day_6: August/02/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya
#From: Asabeneh

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


print(len("python") > len("jargon"))        #output: False
print("on" in "python")                     #output: True


#I hope this course is not full of jargon. Use 'in' operator to check if jargon is in the sentence.
print("jargon" in "This course isn't full of jargon.") #output: True
print(str(float(len("python"))))

print(10 % 2 == 0)                          #output: True and it is even (divisible by 0)


#The floor division of 7 by 3 is equal to the int converted value of 2.7.
val1 =  7 // 3
val2 = int(2.7)
print(val1 is val2)                         #True


#Check if type of '10' is equal to 10
string = '10'
integer = 10
print(string is integer)                    #False
#or,
print(type(string) == type(integer))        #False
#or,
type(string) is type(integer)               #False


#Check if int('9.8') is equal to 10
print('9.8'== 10)                           #False
print(int(9.8) is 10)                       #False