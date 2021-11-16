#accessign values of tuple
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print( "tup1[0]: ", tup1[0])
print( "tup2[1:5]: ", tup2[1:5])

#updating tuple
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# A tuple cannot be updated
# Following action is not valid for tuples
# tup1[0] = 100
# So let's create a new tuple as follows
tup3 = tup1 + tup2
print( tup3)

#deleting tuple elements
tup = ('physics', 'chemistry', 1997, 2000)
print( tup)
del tup
print( "After deleting tup : ")
#print( tup)


#Basic operations
#Length
print(len((1, 2, 3))) #3

#Concatenation
print((1, 2, 3) + (4, 5, 6)) #(1, 2, 3, 4, 5, 6)

#Repetition
print(('Hi!',) * 4 )#('Hi!', 'Hi!', 'Hi!', 'Hi!')

#Membership
print(3 in (1, 2, 3)) #True

#Iteration
for x in (1, 2, 3): print( x) #1 2 3


#indexing, slicing, and matrix
L = ('spam', 'Spam', 'SPAM!')

#Offsets start at zero
L[2] #'SPAM!'

#Negative: count from the right
L[-2] #'Spam'

#Slicing fetches sections
L[1:] #['Spam', 'SPAM!']

#no enclosing delimiters
print( 'abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print( "Value of x , y : ", x,y)

#cmp(t1,t2)
tuple1, tuple2 = (123, 'xyz', 'abc'), ('mno', 'abc')
#print( cmp(tuple1, tuple2))
#print( cmp(tuple2, tuple1))
tuple3 = tuple2 + (786,)
#print( cmp(tuple2, tuple3))


#len(t)
print( "First tuple length : ", len(tuple1))
print( "Second tuple length : ", len(tuple2))

#max(t)
#print( "Max value element : ", max(tuple1))
print( "Max value element : ", max(tuple2))

#min(t)
#print( "min value element : ", min(tuple1))
print( "min value element : ", min(tuple2))

#tuple(seq)
aList = (123, 'xyz', 'zara', 'abc')
aTuple = tuple(aList)
print( "Tuple elements : ", aTuple)