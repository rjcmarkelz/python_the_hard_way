# dicts vs. modules
mydict = {'apple':"I am Apples!"}
print (mydict['apple']) # get apple from dict


import mystuff
mystuff.apple() # get apple from module
print(mystuff.tangerine)

# modules are just key value pairs
# an easy way to access python code

# now create a class in a similar way
class MyStuff(object):
    def __init__ (self):
        self.tangerine = "And now some text"

    def apple(self):
        print("output")

thing = MyStuff() # instantiate
thing.apple()
print (thing.tangerine)

#three ways to get items from things
# dict
mydict['apple']

# import modules
mystuff.apple()
print (mystuff.tangerine)

# making a class
thing2 = MyStuff()
thing.apple()
print (thing2.tangerine)

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["HB2U", "HB2U", "HB2X"])
bulls_parade = Song(["RRF", "PFOS"])

happy_bday.sing_me_a_song()
bulls_parade.sing_me_a_song()






