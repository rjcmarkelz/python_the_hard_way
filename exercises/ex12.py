#rewrite example 11 just using raw_input for all the prompts
age     = raw_input("How old are you in years?")
height  = raw_input("How tall are you in inches?")
weight  = raw_input("How much do you weigh in poinds?")

print "So, your %r years old, %r inches tall, and %r heavy." % (
	age, height, weight)
