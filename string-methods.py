
# capitalize
str = "this is string example....wow!!!";
print("str.capitalize() : ", str.capitalize())

print ("str.center(40, 'a') : ", str.center(40, 'a'))

#count
sub = "i"; # substring to be searched (sub, start, end)
print ("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow";
print ("str.count(sub) : ", str.count(sub))

# encoding 
str = "this is string example....wow!!!";
#str = str.encode('base64','strict');
#print ("Encoded String: " + str.encode('base64','strict'))
#print "Encoded String: " + str;
#print ("Decoded String: " + str.decode('base64','strict'))

# endswith
str = "this is string example....wow!!!";
suffix = "wow!!!";
print (str.endswith(suffix))
print (str.endswith(suffix,20))
suffix = "is";
print (str.endswith(suffix, 2, 4))
print (str.endswith(suffix, 2, 6))


# find
str1 = "this is string example....wow!!!";
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))

# index
str1 = "this is string example....wow!!!";
str2 = "exam";
print (str1.index(str2))
print (str1.index(str2, 10))
#print (str1.index(str2, 20))

#max
str = "this is really a string example....wow!!!";
print ("Max character: " + max(str))
str = "this is a string example....wow!!!";
print ("Max character: " + max(str))

#len 
str = "this is string example....wow!!!";
print ("Length of the string: ", len(str))

#min
str = "this is really a string example....wow!!!";
print ("Min character: " + min(str))
str = "this is a string example....wow!!!";
print ("Min character: " + min(str))


# replace
str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))
print (str.replace("is", "was", 3))


#split
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print (str.split( ))
print (str.split(' ', 1 ))


#startswith

str = "this is string example....wow!!!";
print (str.startswith( 'this' ))
print (str.startswith( 'is', 2, 4 ))
print (str.startswith( 'this', 2, 4 ))

#strip
str = "0000000this is string example....wow!!!0000000";
print (str.strip( '0' ))


#swapcase
str = "this is string example....wow!!!";
print (str.swapcase())
str = "THIS IS STRING EXAMPLE....WOW!!!";
print (str.swapcase())

# title
str = "this is string example....wow!!!";
print (str.title())


# maketrans

#from string import maketrans # Required to call maketrans function.
#intab = "aeiou"
#outtab = "12345"
#trantab = maketrans(intab, outtab)
#str = "this is string example....wow!!!";
#print (str.translate(trantab))


#translate() using maketrans
#from string import maketrans # Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
#trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!";
#print (str.translate(trantab))


#from string import maketrans # Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
#trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!";
#print (str.translate(trantab, 'xm'))


#upper
str = "this is string example....wow!!!";
print ("str.capitalize() : ", str.upper())

#lower
str = "THIS IS STRING EXAMPLE....WOW!!!";
print (str.lower())