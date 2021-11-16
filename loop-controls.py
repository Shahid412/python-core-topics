# Break - loop control
for letter in 'Python': # First Example
	if letter == 'h':
		break
	print ('Current Letter :', letter)

var = 10 # Second Example
while var > 0:
	print ('Current variable value :', var)
	var = var -1
	if var == 5:
		break

# Continue - loop control
for letter in 'Python': # First Example
	if letter == 'h':
		continue
	print ('Current Letter :', letter)

var = 10 # Second Example
while var > 0:
	var = var - 1
	if var == 5:
		continue
	print ('Current variable value :', var)


# Pass - loop control 
for letter in 'Python':
	if letter == 'h':
		pass
		print ('This is pass block')
	print ('Current Letter :', letter)

print ("Completed!")