list = [ 'xyz', 111 , 201, 9.2, 'blank', 70.2, 'king' ]

tinylist = [100, 'chip', 0.01]

# Print complete list
print (list)

# Print first element of the list
print (list[0])

# Print elements starting from 2nd till 3rd
print (list[1:3])

# Print elements starting from 3rd element
print (list[2:])

# Print list two times
print (tinylist * 2 )

# Print concatenated lists
print (list + tinylist) 

# slicing
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

# update
list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

# deleting element
list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ", list1)


#basic operations

#Length
print(len([1, 2, 3])) # 3 

#Concatenation
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6] 

#Repetition
print(['Hi!'] * 4) #['Hi!', 'Hi!', 'Hi!', 'Hi!']

#Membership
print(3 in [1, 2, 3]) #True 
#Iteration
for x in [1, 2, 3]: print (x) #1 2 3


#index, slice, matrix
L = ['spam', 'Spam', 'SPAM!']

#Offsets start at zero
print(L[2]) #'SPAM!'

#Negative: count from the right
print(L[-2]) #'Spam'

#Slicing fetches sections
print(L[1:]) #['Spam', 'SPAM!']


fruits = ['Banana', 'Apple', 'Lime']
# List and the enumerate function
print(list(enumerate(fruits)))