# Day_13: August/09/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:3

# a simple temperature converter:
# a simple program to convert a Fahrenheit temperature to a Celsius temperature:

inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5 / 9
print(f"{cel:.2f}°C")   #[for the degree symbol: Alt + 0176]
#or,
print(f"{round(cel, 2)}°C")

# rewriting this program with try and except:
# catching an exception:
inp = input("Enter Fahrenheit Temp: ")
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5 / 9
    print(f"{cel:.2f}°C")
except:
    print("Please Enter A Number.")
