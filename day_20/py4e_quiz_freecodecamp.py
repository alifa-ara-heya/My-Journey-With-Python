print(0 is 0.0)

for n in "banana":
    print(n)


# What does n equal in this code?
words = "His e-mail is q-lar@freecodecamp.org"
pieces = words.split()
print(pieces)                    # ['His', 'e-mail', 'is', 'q-lar@freecodecamp.org']
parts = pieces[3].split('-')
print(pieces[3])                 # q-lar@freecodecamp.org
print(pieces[3].split('-'))      # ['q', 'lar@freecodecamp.org']
n = parts[1]
print(n)                         # lar@freecodecamp.org

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))