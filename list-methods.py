list1, list2 = [123, 'xyz'], [456, 'abc']

# cmp 
#print( cmp(list1, list2))
#print( cmp(list2, list1))
list3 = list2 + [786]
#print( cmp(list2, list3))

# len
print( "First list length : ", len(list1))
print( "Second list length : ", len(list2))

#max
list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
#print( "Max value element : ", max(list1)) # not supported between str and int
print( "Max value element : ", max(list2))

#min
list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
#print( "min value element : ", min(list1)) # not supported between str and int
print( "min value element : ", min(list2))


#append(obj)
aList = [123, 'xyz', 'zara', 'abc']
aList.append( 2009 )
print( "Updated List : ", aList)

#count(obj)
print( "Count for 123 : ", aList.count(123))
print( "Count for zara : ", aList.count('zara'))

#extend(seq)
bList = [2009, 'manni']
aList.extend(bList)
print( "Extended List : ", aList )

#index(obj)
print( "Index for xyz : ", aList.index( 'xyz' ) )
print( "Index for zara : ", aList.index( 'zara' ) )

#insert(index,obj)
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print( "Final List : ", aList)

#pop()
aList = [123, 'xyz', 'zara', 'abc']
print( "A List : ", aList.pop())
print( "B List : ", aList.pop(2))


#remove(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print( "List : ", aList)
aList.remove('abc')
print( "List : ", aList)

#reverse()
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.reverse()
print( "List : ", aList)

#sort
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
