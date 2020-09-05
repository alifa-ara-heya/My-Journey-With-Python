import mymodule

print(mymodule.generate_full_name('Amatullah', 'Ayesha'))  # Amatullah Ayesha

# Run it in the terminal.

print(mymodule.sum_two_nums(4 , 5))    # 9

print(mymodule.weight(4, 9.8))         # 39.2


# Import Functions from a Module and Renaming
# During importing we can rename the name of the module.
from mymodule import generate_full_name as fullname, sum_two_nums as total
print(fullname('Abdullah', 'Asad'))    # Abdullah Asad
print(total(1, 9))                     # 10


# Import Built-in Modules:
import os
#creating a directory:
os.mkdir('my_diretory')

# Changing the current directory:
os.chdir('G:\Github_Projects\My-Journey-With-Python\day_32')

# Getting current working directory:
print(os.getcwd())  # output: G:\Github_Projects\My-Journey-With-Python\day_32

# Removing directory:
#os.rmdir('G:\Github_Projects\My-Journey-With-Python\day_32')