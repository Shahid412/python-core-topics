var1 = 100

if var1:
	print("1 - Got a true expression value")
	print (var1)
else:
	print("1 - Got a false expression value")
	print (var1)

var2 = 0
if var2:
	print("2 - Got a true expression value")
	print (var2)
else:
	print("2 - Got a false expression value")
	print (var2)


# Single statement suite
if ( var == 100 ) : print ("Value of expression is 100")

# if statement with membership operator
a = 2
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
	print("3 - if with membership operator in - a is available in the given list")
else:
	print("3 - if with membership operator in - a is not available in the given list")
	

# if..elif
var = 100

if var == 200:
	print ("4 - if..elif - Got a true expression value")
	print (var)
elif var == 150:
	print ("5 - if..elif - Got a true expression value")
	print (var)
elif var == 100:
	print ("6 - if..elif - Got a true expression value")
	print (var)
else:
	print ("7 - if..elif - Got a false expression value")
	print (var)

print ("Good bye!")