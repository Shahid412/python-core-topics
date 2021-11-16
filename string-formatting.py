print ("My name is %s and weight is %d kg!" % ('Zara', 21))


# Triple quotes - printed same as it is

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

print ('C:\\nowhere')

# r'expression
print (r'C:\\nowhere')

# Unicode string 
print (u'Hello, world!')

# print integer and float value
print("Yes : %2d, You may come in : %5.2f" % (1, 05.333))
 
# print integer value
print("total employees : %3d, males : %2d" % (240, 120))
 
# print octal value
print("%7.3o" % (25))
 
# print exponential value
print("%10.3E" % (356.08977))


# format()
print('Formatting the {} for "{}!"'.format('Strings', '{Python}'))
 
# format() method with a position 
print('{0} and {1}'.format('Blank', 'Chip'))
 
print('{1} and {0}'.format('Area', 'Main'))
 
 
# f-Strings (same as above)
 
print(f"{'two'} plus \"{'two'} make four!\"")

# combined positional and keyword arguments
print('Do some {0} in {1}, and then {other}.' 
	.format('Coding', 'Python', other ='Smile'))
 
# format() with number
print("Integer :{0:2d}, and float :{1:8.2f}".
	format(12, 00.546))
 
# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".
	format(47.42, 11))
 
print("strings: {a:5d},  lists: {p:8.2f}".
	format(a = 453, p = 59.058))

