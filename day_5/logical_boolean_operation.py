#Day_5: August/01/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya
#Book: Automate the boring staff by Python

print(42 == 42)                        #output: True (checking logical operation)
print(42 > 43)                         #output: False
print(50 > 20)
print(42 == "43")                      #False because the second data type is string
print(42 == 000000042.000000000000)    #True

spam = True
print(type(spam))
print(spam)
print()
print(2 != 3)                          #2 is not equal to 3, so True
print(2 != 2)                          #False

print("spam" == 'spam')                #true
print(True == "True")                  #False
print(True == True)                    #true

eggCount = 42
print(eggCount >= 42)                  #>= greater than or equal to, so true

my_age = 29  
print(my_age <= 50)                    #less than or equal to, so true

print("Cat" == "cat")                  #False
print("cat" == "cat")                  #True

#Boolean Operators:
print(True and True)                   #True
print(True or False)                   #True
print(False or True)                   #True
print()

print('"not" operator:')
print(not True)                        #evaluates to opposite value, so False;
print(not not True)                    #True
print(not not not True)                #False
print(not not not not True)            #True
print(not False)                       #True
print(not not False)                   #False

print((4 < 5) and (5 < 4))             #False, because none of the values is true
print(4 < 5 and 5 < 6)                 #True
print(5 > 4 or 6 > 10)                 #True, because one of the values is true
print(2 + 2 == 4 and 2 + 2 == 5)       #False
print(2 + 2 == 4 and not 2 + 2 == 5)   #True
print(2 + 2 == 4 and not 2 + 2 == 5)   #True    
print(2 + 2 == 4 and 2 + 2 == 5 and 2 * 2 == 2 + 2)         #false   and not > and > or
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)     #true
print(2 + 2 == 4 and not 2 + 2 == 5 and not 2 * 2 == 2 + 2) #false

x = 3
x +=5
print(x)                               #output: 8
print(x == 8 )                         #output: true

x -=6
print(x)                               #output: 2  as,(8-6=2)