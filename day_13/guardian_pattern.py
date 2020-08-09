# Day_13: August/09/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:3

# Short-circuit evaluation of logical expressions:
# guardian pattern: Where we construct a logical expression with additional comparisons to take advantage of the short-circuit behavior.

x = 6
y = 2
print(x >= 2 and x/y > 2)       # True

x = 1
y = 0
print(x >= 2 and (x/y) > 2)     # False  (It proves that the (x/y) has not ben executed due to the short-circuit rule.)

x = 6
y = 0
#print(x >= 2 and (x / y) > 2)  # Traceback

# We can construct the logical expression to strategically place a guard evaluation just before the evaluation that might cause an error as follows:
# When Python is part-way through evaluating a logical expression and stops the evaluation because Python knows the final value for the expression without needing to evaluate the rest of the expression.
x = 1
y = 0
print(x >= 2 and y != 0)        # False

x = 6
y = 0
print(x >= 2 and y != 0 and (x / y) > 2) # False
# In the second expression, we say that y != 0 acts as a guard to insure that we only execute (x/y) if y is non-zero.

#print(x >= 2 and (x / y) > 2 and y != 0) #Traceback.