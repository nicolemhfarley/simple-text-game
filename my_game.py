from sys import exit

# supply room 1 off of dragon room
def supply_room1():
	print "You find a room full of supplies.  Do you want to restock?"
		
	choice = raw_input("yes or no? > ")
		
	if choice == "yes":
		print "You refill your pack and head back to the dragon room"
		return dead_drag()
	elif choice == "no":
		print "You return to the dragon room with nothing"
		return dead_drag()
	else: 
		print "Thanks to your indecision, you return to the dragon room with nothing."
		return dead_drag()

# staircase1 off of dragon room
def staircase1():
	print "You see a staircase leading down into the darkness."
	
	choice = raw_input("Do you: take staircase or go back? > ")
	
	if "staircase" in choice:
		print "You descend down into the darkness."
	elif choice == "go back":
		print "You head back to the dragon room."
		return dead_drag()
	else:
		print "I didn't understand. You head back to the dragon room."
		return dead_drag()

# room guarded by a dragon
def drag_room():
	print "You enter the room and find a dragon. What do you do?"
	
	choice = raw_input("run away or fight dragon? > ")
	
	if "run" in choice:
		print "You scream and run to safety."
	elif "fight" in choice:
		print "You valiently defeat the dragon."
		return dead_drag()
	else: 
		print "You run back into the hallway."
	
# empty dragon room if you already killed it
def dead_drag():
	print "There is a dead dragon still lying on the floor."
	print "You see two doors, one on your left and one on your right.  Would you like to enter one or head back to the hallway?"
	
	choice = raw_input("> ")
		
	if "enter" in choice:
		door = raw_input("Which door, right or left? > ")
				
		if door == "left":
			return supply_room1()
		elif door == "right":
			return staircase1()
		else:
			print "You're too indecisive and return to the hallway."
	elif "door" in choice:
		door2 = raw_input("Which door, right or left? > ")
				
		if door2 == "left":
			return supply_room1()
		elif door2 == "right":
			return staircase1()
		else:
			print "You're too indecisive and return to the hallway."
	elif "back" or "hallway" in choice:
		print "You head back into the hallway." 
	else:
		print "You're too indecisive and head back into the hallway."
				

def quicksand():
	print "Do you want to go through the door?"
	
	choice = raw_input("yes or no? > ")
	
	if choice == "yes":
		print "You fall into quicksand and are sucked down to your death."
		exit(0)
	elif choice == "no":
		print "You turn and walk back down the hallway"
	else:
		print "I didn't understand. You turn and walk back the way you came."
		return hall2()
		
def armory():
	print "You seem to have found an old armory."
	
	choice = raw_input("Do you want to look around for anything useful or turn around? > ")
	
	if "look" in choice:
		print "You find a magical sword. Do you want to take it?"
		take = raw_input("> ")
		if take == "yes":
			print "You feel a rush of power as you pick it up."
			print "now you head back into the hallway."
			return start()
		elif take == "no":
			print "You don't find anything else useful and return to the hallway"
		else:
			print "You failed to make a decision. You head back the way you came."
	elif "turn" in choice:
		print "You head back the way you came."
	else:
		print "You can't decide? You head back the way you came."

# room after killing witch
def dead_witch():
	print "The dead witch lies in the middle of the room."
	print "You see two doors. One to the left and one to the right. Do you want to go through one of them?"
		
	door_choice = raw_input("> ")
	
	if door_choice == "yes":
		print "Which door?  right or left?"
			
		door = raw_input("> ")
			
		if door == "right":
			return right_door()
		elif door == "left":
			return left_door()
		else:
			print "You turn and head back into the hallway."
			return start()
	else:
		print "You turn and head back to the hallway."
		return start()

# left_door off of the witch room: staircase upwards
def left_door():
	print "The door on the right open into a stairwell heading up. Would you like to take it?"
	
	choice = raw_input("> ")
	
	if choice == "yes":
		print "You head up into the dark only to find a dead end."
		print "You turn and head back into the witch room."
		return dead_witch()
	else:
		print "You turn and head back into the witch room."
		return dead_witch()

# right_door off of the witch room: gold room
def right_door():
	print "This room is full of gold. Do you want to take some?"
	
	choice = raw_input("> ")
	
	if choice == "yes":
		print "You fill all of your pockets with gold and head back into the witch room."
		return dead_witch()
	else:
		print "You turn and head back into the witch room empty handed."
		return dead_witch()

def witch_room():
	print "You open the door to see an evil witch bending over a smoking cauldron.  What do you want to do?"
		
	choice = raw_input("Fight the witch or turn and run? > ")
	
	if "fight" in choice:
		print "You kill the evil witch!"
		return dead_witch()	
	elif "run" or "turn" in choice:
		print "You run back into the hallway and slam the door behind you."
	else:
		print "You return to the hallway."

#2nd hallway w/ quicksand and finish at the end
def hall2():
	print "You turn and walk down this second hallway."
	print "There's a door to your right and another straight ahead." 
	print "Would you like to open a door or go home?"
	
	choice = raw_input("> ")
	
	if "door" in choice:
		print "Which door would you like to open, the one on the right or the one straight ahead?"
		door = raw_input("> ")
		if "right" in door:
			return quicksand()
		elif "ahead" in door:
			print "You win the game!"
			exit(0)
	else:
		print "You run home."
		exit(0)


def start():
	print "You find yourself in a long hallway with a door on either side of you."
	print "Do you want to continue down the hallway or enter a door?"
	
	choice = raw_input("> ")
	
	if "door" in choice:
		door = raw_input("Which door, left or right? > ")
		if door == "left":
			return armory()
		elif door == "right":
			return witch_room()
		else:
			print "Not feeling that adventurous? You continue down the hall."
	elif "hallway" in choice:
		print "You continue down the hall until you reach a door."
		print "There's another hallway to the right."
		print "Do you want to go through the door or turn right?"
		
		choice2 = raw_input("> ")
		
		if "door" in choice2:
			return drag_room()
		elif "turn" in choice2:
			return hall2()
		else:
			print "I didn't understand"
		
	else:
		print "You didn't make a decision.  I guess it's time to go now."
		exit(0)

#drag_room()
#supply_room1()
#staircase1()
#quicksand()
#armory()
#witch_room()
start()
