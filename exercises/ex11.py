print "How old are you in years?",
age = float(raw_input())
print "How tall are you in inches?",
height = float(raw_input())
print "How much do you weigh in lbs?",
weight = float(raw_input())

print "So, your %r years old, %r inches tall and %r pounds heavy." % (
	age, height, weight)

bmi = float(height/weight) # without using float the answer rounds
print "Your body mass index is: %r" % (bmi)