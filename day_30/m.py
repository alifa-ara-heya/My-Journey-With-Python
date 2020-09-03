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


def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	if len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	elif len(word1) == len(word2) == len(word3):
		word = word1
	return word

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))