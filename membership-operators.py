a = 100
b = 20
list = [1, 2, 3, 4, 5 ]

# Membership operators
if ( a in list ):
	print("1 - in - a is available in the given list")
else:
	print("1 - in - a is not available in the given list")
	
# Logical not in - membership operator
if ( b not in list ):
	print("2 - not in - b is not available in the given list")
else:
	print("2 - not in - b is available in the given list")
	

a = 2
if ( a in list ):
	print("3 - in - a is available in the given list")
else:
	print("3 - in - a is not available in the given list")
	
# Logical or 
if ( a in list or b in list):
	print("4 - or - either a or b is available in the given list")
else:
	print("4 - or - a and b are not available in the given list")
