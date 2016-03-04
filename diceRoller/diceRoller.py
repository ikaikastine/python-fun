import sys, random

def roll():
	randInt = random.randint(1, 6)
	print "Dice rolls:", randInt

if __name__ == '__main__':
	prompt = raw_input("Would you like to roll the dice? ")
	if (prompt == "yes" or prompt == "y"):
		roll()
		again = raw_input("Roll again? ")
		while(again == "yes" or again == "y"):
			roll()
			again = raw_input("Roll again? ")
	else:
		print "Have a nice day"