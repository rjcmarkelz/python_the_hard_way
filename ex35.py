#Branches and functions

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you are not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard! A curse on you for the rest of your days!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input(">  ")

		if next == "take honey":
			dead("The bear looks at you and slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
			gold_room()
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		else:
			print "I have no idea what that means. Try 'take honey' or 'taunt bear' "

def cthulu_room():
	print "Here you see the great evil Cthulhu."
	print "He, she, it, whatever stares ar you and you go insane."
	print "Do you flee for your life or eat your head?"

	next = raw_input("> ")

	if "flee" in next:
		print "Good choice. While running away you stumbled upon a treasure room."
		gold_room()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		dead("Insanity!!!!!")

def dead(why):
	print why, "Your dead! Start over!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and door to your left."
	print "Which to do you take right or left?"

	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You did not choose? You stumble around the room until you starve!")

start()


















