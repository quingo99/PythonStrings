#pythong Strings

#Pythong is loosly type -- data types

#String variableName -- Java C++ Swift Most OBJ  Oriented Languages
# variableName =  "This is a string" --> String
# variableInt = 34 --> Integer

# Python 
# variableName =  "This is a string" --> String
# variableInt = 34 --> Integer

# Python is scripting language
# Python can run on anything that allows the interpreter to be installed

# Does not require compile 
# You won't know that failure of the code until you run it
# Slower to run through the interpreter

# String is a list of characters
# ---- Character [a-z. A-Z]
# --- Number[0-9]
#--- Special Character[*&(^)]
#-- Space [' ']
# --- Escape Character [\n -->Newline, \t -- tab, \\]

school = 'WEBER STATE'

print ('First Character is: ', school[0])
print ('Second Character is: ', school[1])
print ('Last Character is: ', school[-1])
print ('Second to Last Character is: ', school[-2])

first_name = 'Qui';
last_name= 'Ngo';
initials = 'Initials: ', first_name[0], last_name[0];

first_initials = first_name[0], first_name[1], first_name[2]
last_initials = last_name[0]

##print(initials)
##print('Initials: ', first_initials + last_initials)

first_three_first_name= first_name[0:3]

print('First three first name: '+ first_three_first_name)


capital_name =first_name.upper()
print("capital name: ", capital_name)