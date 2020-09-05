stuff = dict()
print(stuff.get('candy',-1))   # -1

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)

print('big' > 'small')
print(11 % 5)



def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))