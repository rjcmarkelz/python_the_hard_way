the_count = [1, 2, 3, 4, 5]
fruits    = ['apples', 'oranges', 'pears', 'apricots']
change    = [1, 'pennies', 2 , 'dimes', 3, 'quarters']

#these for-loops go through the list
for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

#mixed lists
#use %r because we do not know if string or number
for i in change:
	print "I got %r" % i

# build an empty list
elements = []

#then use a range function to populate the list
for i in range (0, 6):
	print "Adding %d to the list." % i
	#append to populate the list
	elements.append(i)

#now to print them
for i in elements:
	print "Element was: %d" % i

	