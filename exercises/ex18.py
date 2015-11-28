# this one is like your scripts with argv
# first we tell python we want to make a function "Define" it
# then we give the function a name
# then we tell it what we want it to do inside the parenthesis
# after the colon it starts indenting indicating that all components
# that are indented are attached to this argument
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# the *args is pointless and instead we can do the following
# we can skip the whole unpacking of arguments and just put them
# inside the parenthesis
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Cody", "Markelz")
print_two_again("Cody", "Markelz")
print_one("First!")
print_none()
