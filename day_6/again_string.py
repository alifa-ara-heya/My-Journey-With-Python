#Day_6: August/02/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya
#Topic: index, isupper function, file and replace function

course = 'python for beginners by Mosh'

print(course[0])

name = "Alifa ara Heya"
#index
print(name[0])         #output: A (0 is the index here)
print(name[1])         #output: l
print(name[2])         #output: i
print(name[3])         #output: f
print(name[4])         #output: a
print()
print(name[-1])        #output: a, (-1 index starts counting from last.)
print(name[-2])        #output: y
print(name[-3])        #output: e
print(name[-4])        #output: H
print(name[-5])        #output: 'space'
print(name[-6])        #output: a

sentence = "You are beautiful."
           #0123456789
print(sentence[0 : 3])     #output: You
print(sentence[0 : ])      #output: You are beautiful. (the default end index is 0)
print(sentence[4 : 7])     #output: are
print(sentence[8 : ])      #output: beautiful.
print(sentence[0 : 7])     #output: You are
print(sentence[: 7])       #output: You are   (the default start index is 0)

another_sentence = sentence
print(another_sentence)             #output: You are beautiful.

another_sentence = sentence[:]
print(another_sentence)             #output: You are beautiful.

#find and replace:
print(sentence.find("beautiful")) #output: 8
print(sentence.replace("beautiful", "absolutely beautiful"))  #output: You are absolutely beautiful.
print('beautiful' in sentence)    #output: True   (in is an operator which produces Boolean value)
print('ugly' in sentence)         #output: False

name = "Jennifer"
print(name[0 : 1])     #output : J
print(name[0 : -1])    #output: Jennife
print(name[1 : -1])    #output: ennife
print(name[-1])        #output: r
print(name[1])         #output: e
print()

print(name.find('e'))  #output: 1
print(name.find('E'))  #output: -1   .find method is case sensitive.
print(name.find('J'))  #output: 0 because, the index no of J is 0 here.
print(name.find('f'))  #output: 5


#.isupper method:
print(name.isupper())  #False
name = name.upper()
print(name)            #JENNIFER
print(name.isupper())  #True
print(len(name))       #8

#.index method to find the index number:
print(name.index("J")) #index num: 0
print(name.index("E")) #index num: 1
print(sentence.index("beautiful")) #index num: 8