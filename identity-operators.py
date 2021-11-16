a = 20
b = 20

if ( a is b ):
	print("1 - is - a and b have same identity")
else:
	print("1 - is - a and b do not have same identity")

if ( id(a) == id(b) ):
	print("2 - id() - a and b have same identity")
else:
	print("2 - id() - a and b do not have same identity")

b = 30
if ( a is b ):
	print("3 - is - a and b have same identity")
else:
	print("3 - is - a and b do not have same identity")

if ( a is not b ):
	print("4 - is not - a and b do not have same identity")
else:
	print("4 - is not - a and b have same identity")
