#Goal is to generate completely random agency name
#Generates an agency name of n characters

import string
import random
def acro(size=3, chars=string.ascii_uppercase):
	return ''.join(random.choice(chars) for i in range (size))
print acro()

#Goal is to generate agency name related to extant agency or set of agencies

print acro(3, "SEC")


#Pin first two letters

def cro(size=1, chars=string.ascii_uppercase):
     return ''.join("SE" + random.choice(chars) for i in range (size))

#Pin first letter and recurring letter
#size is multiplied times two

def cro(size=2, chars=string.ascii_uppercase):
	return ''.join("S" + random.choice(chars) for i in range (size))
print cro()
