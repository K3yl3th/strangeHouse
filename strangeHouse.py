# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:50:44 2019

@author: Marianne Dery
"""

#THE GAME COMPONENTS

import matplotlib.pyplot as plt
import matplotlib.patches as patches

#rect = patches.Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none')

def instructions():
	print("""   ---Strange House---
	   
   You woke up in your house, but it seems a bit strange. Some things seem different then they were yesterday, others appeared and some disappeared. Uneasy, you decided to get out, but the front door is locked. What will you do?
   
   ----------
		
   Commands:
       go [direction] : Move from one room to another
       examine [object] : Get more information on an object present in the room
		   tip: You could get clues!
       interact [object] : Interact with an object in the room
	   access [object] : Acces an object within your inventory  
	   
       instructions : Present this menu
       status: Tells you which room you are in as well as what your inventory contains
       description : Short description of the room you are in 
	   
	   leave: While doing a puzzle, allows you to leave the puzzle and return to the room you were in.
       exit: Exit the game
	       P.S. The game can't be saved. All progress will be lost if you quit.
	   
   ----------
	""")
		
def status(room):
	print('\n    ---Status---\n')
	print("    You're in the " + room.nameRoom)
	print("    Inventory: " + str(inventory))
	print("\n    ----------")
	
def changeRoom(move, currentRoom):
	newRoom = currentRoom    		#defines the new room. if the room can't be change, it will stay as the current room
	try: 			#makes sure the user added a direction after 'go' (raises an error if there is no argument)	
		if currentRoom.connection[move[1]] == 'none':			#if there's no connection to other rooms, tell the user
			print('\nThere is nothing there.')
		else:
			if currentRoom.connection[move[1]].unlocked:		#if there is a connection and it is unlocked, updates the room
				newRoom = currentRoom.connection[move[1]]
				status(newRoom)
				if newRoom.unvisited:		#if the room has never been visited, prints out the description of the room	
					newRoom.enterRoom()     #(other wise, the user will have to ask for the description)
			else:		   	     #if the room is locked, say so and does not change the room
				print("\nSeems like this door is locked! You'll need a key")
	except:
		print("\nThe direction isn't valid. Enter go <cardinalDirection>")
		newRoom = currentRoom
	return newRoom

def examinateItem(move, currentRoom):
	try:			#makes sure the user added an item to examinate (will raise an error if there is no argument)
		if move[1] in currentRoom.items:		#makes sure the room contains the item the user wants to examinate
			currentRoom.items[move[1]].examinate()		#fetch the description given for the object being examined
		else:
			print("\nYou can't find this object. Is it the right one?")
	except:
		print("\nThe command is written 'examine [object]'. Verify your input.")
		
def interactItem(move, currentRoom):
	try:		#makes sure the player has added an input after the command
		if move[1] in currentRoom.items:		#verifies if the abject exists within the room
			currentRoom.items[move[1]].interact()		#calls the function to interact with the object
		else:
			print("\nYou can't find this object. Is it the right one?")
	except:
		print("\nThe command is written 'interact [object]'. Verify your input.")
		
def accessItem(move, currentRoom):
	try:		#makes sure the player added an item to access
		if move[1] in inventory:		#checks if the player has the item with them
			if inventoryAccess.items[move[1]].examination == "\nThere is nothing interesting about this object":
						#verifies wether the inventory calls for a description(examination) or a function(interaction)
				inventoryAccess.items[move[1]].interact()
			else:
				inventoryAccess.items[move[1]].examinate()
		else:
			print("\nYou can't find this object. Is it the right one?")
	except:
		print("\nThe command is written 'acces [object]'. Verify your your input.")

class room:
	def __init__(self, nameRoom, unlocked):
		self.nameRoom = nameRoom
		self.unlocked = unlocked
		self.connection = {
				'north' : 'none',
				'east' : 'none',
				'south' : 'none',
				'west' : 'none'
				}
		self.items = {}
		self.unvisited = True
		self.description = "\nThere is no description available for this room."
	
	def addItem(self, itemName, item):
		self.items[itemName] = item
	
	def addConnection(self, direction, room):
		self.connection[direction] = room
	
	def addDescription(self, desc):
		self.description = desc
	
	def printDescription(self):
		print(self.description)
	
	def unlockDoor(self):
		self.unlocked = True
	
	def enterRoom(self):
		print(self.description)
		self.unvisited = False
	
class item:
	def __init__(self, itemName, room):
		self.itemName = itemName
		self.room = room
		self.examination = "\nThere is nothing interesting about this object"
		self.interaction = 'none'
		self.canInteract = True
	
	def addExamination(self, comment):
		self.examination = comment
	
	def examinate(self):
		print(self.examination)
	
	def addInteraction(self, interaction):
		self.interaction = interaction
		
	def interact(self):
		if self.interaction == 'none':
			print("\nHmm, there's nothing to do with this object.")
		else:
			self.interaction()
	
	def cantInteract(self):
		self.canInteract = False

#This function is necessary when creating an item. It adds the item in the room's dictonary containing all the items
#Links the item's name to it's variable so it can be called easily when the user specifies and item to interact with
def activateItem(item):
	for name in item.itemName:
		item.room.items[name] = item


#CREATING THE PUZZLES FOR THE GAME


def interactCoat():
	
	if coat.canInteract:		#If the picture has already been taken, you can't interact with the coat anymore
		
		if livingRoom.unvisited:		#Presents a different text depending on wether the player has seen the painting or not
			print("\nThere's a picture in the left pocket of your coat. There's three kids on the picture and a small text is written on the back: 'Emily: 3years Sasha: 6years Thomas: 9years'. Who are these kids?")
			inventory.append('picture') 
			status(currentRoom)			
		else:
			print("\nThere's a picture in the left pocket of your coat. You recognize the three kids from the portait in the living room. A small text is written on the back: 'Emily: 3years Sasha: 6years Tomhas: 9years'.")
			inventory.append('picture')
			status(currentRoom)
		coat.cantInteract()		#locks the interaction
	else:
		print("\nYou've already taken this object.")
		
def interactCouch():
	
	if couch.canInteract:		#if the money hasn't already been taken, gives it
		print("\nWhen you searched through the couch's cushions, you found 2.43$, great! Not that it seems all that helpful...")
		inventory.append('money')
		status(currentRoom)
		couch.cantInteract()
	else:
		"There's no more money."
		
def interactOven():
	print("\nThe time on the oven isn't the same as the one on your watch. It indicates that it's 15:56. You try to change it, but for some reason it won't let you. That's strange.")	
	
def interactFridge():
	print("\nSeems like someone recently did the gorceries. You have so many food items which you didn't have yesterday: 6 eggs, 2 cakes, 3 chicken breast and 5 zucchinis. What recipe could they be for?")
	
def interactCounter():
	print("\nThere's a fruit bowl in the middle of the counter. That's not yours, you've never liked fruits. Someone bought 2 bananas, 3 apples and 5 oranges.")

	
def interactDrawing():		#prints out a circle, a square and two triangles
	circle = plt.Circle((0.125, 0.5), 0.1, color='r')
	rec = patches.Rectangle((0.26, 0.4), 0.23, 0.2, linewidth = 1, edgecolor = 'blue', facecolor = 'blue')
	fig, ax = plt.subplots()
	ax.add_artist(circle)
	ax.add_patch(rec)
	ax.add_patch(patches.Polygon([[0.51, 0.4],[0.625, 0.6],[0.74, 0.4]], closed=True,fill=True, color = 'green')) 
	ax.add_patch(patches.Polygon([[0.76, 0.4],[0.875, 0.6],[0.99, 0.4]], closed=True,fill=True, color = 'green')) 
	plt.show()

def interactPiggyBank():
	money = 5.65
	moneyCoach = 2.43
	
	if piggyBank.canInteract:		#makes sure the money hasn't already been put in
		if 'money' in inventory:		#makes sure the player has money to put in the piggy bank
			money = money + moneyCoach
			print("\nYou try to put the money in the piggy bank. Great you now have "  + str(money) + "$.")
			piggyBank.cantInteract()
			inventory.remove('money')
			status(currentRoom)
		else:
			print("\nIt says there is" + money + "$. I wonder if it still works... It's a shame I don't have any money to put in it")
	else:
		money = money + moneyCoach
		print("\nYou've already put all the money you had. You have " + money + "$." )

def interactPainting():
	code = 936		#the code for the safe
	
	if painting.canInteract:		#makes sure the puzzle hasn't been solved already
		print("\nAs you approach the painting, you realise there are hinges on the left side. You wonder if there's something hidden behind... And there is! It's a safebox and it requires a combination made out of three numbers. What could it be?")
		
		while True:
			guess = input("\nYour code:\n-->")
			guess = guess.replace(" ", "")
			
			try:		#makes sure the input is numbers
				if int(guess) == code:
					print("\nThe safe is unlocked!\nInside, there's a grocery list.\n\n  To buy:\n    -oranges\n    -eggs\n    -chicken\n    -bananas\n\nSeems like everything's strange here.")
					inventory.append('groceries')
					status(currentRoom)
					break
				elif len(guess) != 3:		#tell the user if the code isn't the appropriate lentgh
					print("\nThe combinations has to be 3 numbers.")
				else:
					print("\nThe safe won't open. Seems like the combination was wrong.")
			except:
				if guess == 'leave':		#allows the user to leave the puzzle for more clues
					status(currentRoom)
					break
				print("\nYou can't add letters to the combination.")
	else:
		print("\nYou've already completed this puzzle!")			

def interactKeypad():
	code = 1556
	 
	if keypad.canInteract:		#makes the puzzle hasn't been solved
		print("\nthe display of the keypad shows:\n_ _ : _ _\nWhat could be the code?")
		
		while True:
			guess = input("\nYour code:\n-->")
			guess = guess.replace(" ", "")
			
			try:		#makes sure the code is made out of numbers
				if int(guess) == code:		#verifies if the code is right
					print("\nThe pinpad's display turned green! That must be a good sign. Let's see if the door is now unlocked.")
					bathroom.unlockDoor()
					status(currentRoom)
					break
				elif len(guess) != 4:		#if the code isn't long enough, says so
					print("\nThe combination has to be 4 numbers.")
				else:
					print("\nThe display turned red. Must mean the combination was wrong.")
			except:
				if guess == 'leave':
					status(currentRoom)
					break
				print("\nYou can't add letters to the combination.")
				
def interactComputer():
	code = 8.08
	
	if computer.canInteract:		#makes sure the puzzle hasnt alreday been solved
		print("\nOnce you're close enough to the computer, you can see which page it is open on. It seems to be a bank website, though you've never heard of this one. It is called PocketMoney. Not very convincing. The webpage displays:\n")
		print("""	----------
		
Your account number: 7382937482
Your name: John Doe
Your Address: *** mystery street
Your balance: _I_____
	
[Submit]
		
	----------
		
		Strangely enough, all the information seems correct.""")
		guess = input('Your code:\n-->')
		guess = guess.replace(" ", "")
		
		while True:
			try:
				if float(guess) == code:
					print("\nReward? What reward? your printer suddenly opens and starts printing this:")
					circle = plt.Circle((0.125, 0.5), 0.1, color='r')
					rec = patches.Rectangle((0.26, 0.4), 0.23, 0.2, linewidth = 1, edgecolor = 'blue', facecolor = 'blue')
					fig, ax = plt.subplots()
					ax.add_artist(circle)
					ax.add_patch(rec)
					ax.add_patch(patches.Polygon([[0.51, 0.4],[0.625, 0.6],[0.74, 0.4]], closed=True,fill=True, color = 'green')) 
					ax.add_patch(patches.Polygon([[0.76, 0.4],[0.875, 0.6],[0.99, 0.4]], closed=True,fill=True, color = 'green')) 
					plt.show()
					print("\nWhat is it?? As strange as it is, you decide to keep it. Who knows? It might be useful.")
					inventory.append('drawing')
					status(currentRoom)
					break
					
			except:
				if guess == 'leave':
					status(currentRoom)
					break
				else:
					print("\nThe input has to be a number.")
					guess = input('\nYour code:\n-->')
		else:
			print("\nYou've already completed this puzzle.")
					
def interactToys():
	code = ['circle', 'square', 'triangle', 'triangle']
	
	if toys.canInteract:
		print("\nYou take the toy you think looks the most interesting. It's a simple game where you need to select a combination of 4 inputs made out of circles, squares and triangles. Intrigued, you decide to play. You look all around the toy but no clues. What could be the combination?")
		
		while True:
			guess = input('\nYour code:\n-->')
			guess = guess.lower()
			guess = guess.split()
			guess = list((guess))
			
			if len(guess) == 1 and guess[0] == 'leave':
				status(currentRoom)
				break
			elif len(guess) == 4:
				if guess == code:
					print("\nAs soon as change your last input for a " + code[-1] +", the toy opens and a key drops on the ground. It must be for the last locked room! You start to get all excited, as you approach the end of this nightmare.")
					inventory.append('key')
					status(currentRoom)
					toys.cantInteract()
					break
				elif (guess[0] == 'square' or 'circle' or 'triangle') and (guess[1] == 'square' or 'circle' or 'triangle') and (guess[2] == 'square' or 'circle' or 'triangle') and (guess[3] == 'square' or 'circle' or 'triangle'):
					print("\nYou try to open the toy, all excited, but it won't budge. You've got the wrong combination")
				else:
					print("\nThe code is made out of 4 objects, each of them being either a square, triangle or circle.\nExample of correct input: circle circle circle square")
			else:
					print("\nThe code is made out of 4 objects, each of them being either a square, triangle or circle.\nExample of correct input: circle circle circle square")
	else:
		print("\nYou've already completed this puzzle")
		
def interactLunchBox():
	code = 5632
	 
	if keypad.canInteract:
		print("\nThe lunchbox is locked. Great. The lock looks like the one used for school lockers. The combination is made out of 4 numbers.")
		
		while True:
			guess = input("\nYour code:\n-->")
			guess = guess.replace(" ", "")
			
			try:
				if int(guess) == code:
					print("\nIt unlocked, great! Inside the lunchbox, you find a big godlen key. Could it be the key for the front door??")
					inventory.append('goldenKey')
					status(currentRoom)
					break
				elif len(guess) != 4:
					print("\nThe combination has to be 4 numbers.")
				else:
					print("\nThe lock didn't budge.")
			except:
				if guess == 'leave':
					status(currentRoom)
					break
				print("\nYou can't add letters to the combination.")
	

def interactLock():
	if lock.canInteract:
		if 'key' in inventory:
			print("\nIt worked! The door is now unlocked.")
			bedroom.unlockDoor()
			inventory.remove('key')
			lock.cantInteract()
			status(currentRoom)
		else:
			print("\nYou need a key to unlock the door or something heavy to break it.")
	else:
		print("\nYou've already unlocked the door.")
		
def interactEndLock():
	if 'goldenKey' in inventory:
		print("""    ----------
Uneasy and yet really excited, you try to unlock the door. You're a bit scared. What if the key doesn't work? If it does, that's on the other side of the door, do you really want to know? Still, you try it in hope to end all this madness. The key fits perfectly. You're shaking. Is it exctitment or fear? It's hard to tell. You turn the key and the lock drops to the ground with a loud 'bang'. You open the door quickly and you see the outside world, unchanged. Normal. Reassuring. You start running away, never looking back to the damned house.

    ----------""")
		print("\nTHE END.")
		end.unlockDoor()
	else:
		print("\nYou need a key to unlock this door.")
 

#SETING UP THE ROOMS


entrance = room('entrance', True)
bathroom = room('bathroom', False)
livingRoom = room('living room', True)
kitchen = room('kitchen', True)
bedroom = room('bedroom', True)

end = room('outise world', False)
inventoryAccess = room('inventory', False) 		#the inventory is set up as a room since rooms already have a way
												#of accessing items and calling their description

entrance.addDescription("\nYou're standing in the entrance. In front of you is the exit door, which is sadly locked. To your left, you see your coat hanger. To the right is another door with a keypad and if you look behind you there is the living room")
entrance.addConnection('east', bathroom)
entrance.addConnection('south', livingRoom)
entrance.addConnection('north', end)

bathroom.addDescription("\nLike all bathrooms, you can see a bath to the front and a sink and a toilet to your right. You cannot see any other doors than the one one you came from, to the left.")
bathroom.addConnection('west', entrance)

livingRoom.addDescription("\nA big couch occupies most of the room, it's facing to the west wall where a big family panting is hanged. In the middle of the room, you also see a big mess of childrens' toys. To your right, you can see your kitchen and behind you is the door leading to your bedroom. However, the door is now locked.")
livingRoom.addConnection('north', entrance)
livingRoom.addConnection('south', bedroom)
livingRoom.addConnection('east', kitchen)

kitchen.addDescription("\nIn the midlle of the kitchen is a small table. You didn't have enough money to buy a big fancy one. Your paperwork and computer are still there. Behinf the counter, against the right wall, you can see all your old appliances. To your right, you see the living room you just left.")
kitchen.addConnection('west', livingRoom)


bedroom.addDescription("\nIn the middle of the room is your bed, against the south wall. Beside each side of the bed there's two side tables. To your left, there is a wardrobe and in front of you is the door you came from.")
bedroom.addConnection('north', livingRoom)


#SETTING UP THE ITEMS


		#entrance

coat = item( list(('coat', 'coats','hanger')), entrance)
coat.addExamination("\nYour coat's hanged there. You wonder if you left anything important in it...")
coat.addInteraction(interactCoat)
activateItem(coat)

keypad = item(list(('keypad',)), entrance)
keypad.addExamination("\nThe keypad seems to unlock the door which leads to the bathroom (At least, you hope your bathroom is still behind there). The keypad seems to take 4 numbers as a combination, since the electronic display shows:\n_ _ : _ _")
activateItem(keypad)
keypad.addInteraction(interactKeypad)

endLock = item(list(('lock', 'door')), entrance)
endLock.addExamination("\nThere's a massive lock unabling you to get out. You'll need to find a key")
endLock.addInteraction(interactEndLock)
activateItem(endLock)

	#bathroomp
	
sink = item(list(('sink',)), bathroom)
activateItem(sink)
	
bath = item(list(('bath',)), bathroom)
bath.addExamination("\nAs you approach the bath, you can see something pink inside. What could it be? You get closer and see a small porcelaine pig. You realise it's a piggy bank.")
activateItem(bath)
	
toilet = item(list(('toilet',)), bathroom)
activateItem(toilet)
	
piggyBank = item(list(('piggy', 'bank')), bathroom)
piggyBank.addExamination("\nIt's the piggy bank you used to collect cents when you were younger. You liked it very much, since there was a display wich would show how much money you had. Maybe there's some money in it right now?")
piggyBank.addInteraction(interactPiggyBank)
activateItem(piggyBank)

	#livingRoom

couch = item(list(('couch',)), livingRoom)
couch.addExamination("\nThe couch is the same as it has always been. Old, but comfortable. With a bit of luck, something useful could have been lost between the cushions")
couch.addInteraction(interactCouch)
activateItem(couch)
	
painting = item(list(('painting', 'portrait')), livingRoom)
painting.addInteraction(interactPainting)
painting.addExamination("\nHmmm... That wasn't there before! On the left there's a boy and a girl is on the right. They both have their hands on a yonguer girl who's in the middle. She almost look like a baby. Maybe a younger sister? Those three people aren't part of your family... Why is it there?")
activateItem(painting)

toys = item(list(('toys', 'toy', 'bedroom')), livingRoom)
toys.addExamination("\nYou don't have a kid. What could these be for?")
toys.addInteraction(interactToys)
activateItem(toys)

lock = item(list(('lock', 'door')), livingRoom)
lock.addExamination("\nLooks like a normal lock. You'll need either the key or something heavy to break it.")
lock.addInteraction(interactLock)
activateItem(lock)

	#Kitchen

table = item(list(('table',)), kitchen)
activateItem(table)

computer = item(list(('computer', 'pc')), kitchen)
computer.addExamination("\nYour good old computer which has never let you down (except that one time in 12th grade where you lost all your documents), is left open on the table. You see a faint light comming from it, indicating that it is open.")
computer.addInteraction(interactComputer)
activateItem(computer)

fridge = item(list(('fridge', 'refrigerator')), kitchen)
fridge.addExamination("\nSeems like someone recently did the gorceries. You have so many food items which you didn't have yesterday: 6 eggs, 2 cakes, 3 chicken breast and 5 zucchinis. What recipe could they be for?")
fridge.addInteraction(interactFridge)
activateItem(fridge)

oven = item(list(('oven',)), kitchen)
oven.addExamination("\nThe time on the oven is at 15:56. Strange, that's not what your watch says.")
oven.addInteraction(interactOven)
activateItem(oven)

paperWork = item(list(('paper', 'work', 'paperwork', 'papers')), kitchen)
activateItem(paperWork)

sinkKitchen = item(list(('sink',)), kitchen)
activateItem(sinkKitchen)

counter = item(list(('counter',)), kitchen)
counter.addExamination("\nThere's a fruit bowl in the middle of the counter. That's not yours, you've never liked fruits. Someone bought 2 bananas, 3 apples and 5 oranges.")
counter.addInteraction(interactCounter)
activateItem(counter)

appliances = item(list(('appliance', 'appliances')), kitchen)
appliances.addExamination("\nYou find the basics in your kitchen: an oven, a fridge and a sink. Nothing too fancy.")
activateItem(appliances)

	#bedroom

bed = item(list(('bed',)), bedroom)
activateItem(bed)

sideTable = item(list(('side', 'table', 'tables')), bedroom)
sideTable.addExamination("\nOn one table, there is a kid's lunchbox. Obviously not yours. On the other one, there's a basic lamp.")

lamp = item(list(('lamp',)), bedroom)
activateItem(lamp)

lunchBox = item(list(('lunch', 'box', 'lunchbox')), bedroom)
lunchBox.addExamination("\nIt is a kid's lunchbox. Again, not your kid since you don't have one. What is it doing there?")
lunchBox.addInteraction(interactLunchBox)
activateItem(lunchBox)

wardrobe = item(list(('wardrobe', 'clothe', 'clothing', 'clothes', 'closet')), bedroom)
activateItem(wardrobe)

	#inventory

picture = item(list(('picture',)), inventoryAccess)
picture.addExamination("\nThe three kids are the same as the one in the living room's painting. On the back si written their name and ages: 'Emily: 3years Sasha: 6years Thomas: 9years'.")
activateItem(picture)

groceryList = item(list(('groceries',)), inventoryAccess)
groceryList.addExamination("\nTo buy:\n  -oranges\n  -eggs\n  -chicken\n  -bananas")
activateItem(groceryList)

money = item(list(('money',)), inventoryAccess)
money.addExamination("\nYou have 2.43$.")
activateItem(money)

drawing = item(list(('drawing',)), inventoryAccess)
drawing.addInteraction(interactDrawing)
activateItem(drawing)

key = item(list(('key',)), inventoryAccess)
key.addExamination("\nThe key used to unlock the bedroom.")
activateItem(key)

goldenKey = item(list(('goldenKey')), inventoryAccess)
goldenKey.addExamination("\nThe key to end it all.")
activateItem(goldenKey)

#MAIN PROGRAM


#Sets the player's starting point and inventory
currentRoom = entrance
inventory = list()

#Gives the information necessary for the player to understand the game
print(instructions())
status(currentRoom)
entrance.enterRoom()

while True:
	
	move = input('\n--> ')
	move = move.lower().split()
	
	#verifies the player has entered an action
	while True:
		try:
			move[0]
		except:
			print("\nThe command isn't valid. For a list of all commands, write 'instructions'")
			move = input('\n--> ')
			move = move.lower().split(" ")
		else:
			break
		
	#Finds the move the user wants to do and applies it
	if move[0] == 'go':		#if the command is go, change the currentRoom to the one present in the direction mentionned
		currentRoom = changeRoom(move, currentRoom)
	
	elif move[0] == 'instructions':		#prints out the instructions
		instructions()
		
	elif move[0] == 'examine':		#prints out a description of the object
		examinateItem(move, currentRoom)
	
	elif move[0] == 'interact':		#brings out a puzzle or gives an item
		interactItem(move, currentRoom)
		
	elif move[0] == 'access':		#acces an item in the inventory(gives back the description)
		accessItem(move, currentRoom)
		
	elif move[0] == 'status':		#prints out the player's status
		status(currentRoom)
	
	elif move[0] == 'description':		#describes the room
		print(currentRoom.description)
	
	elif move[0] == 'exit':
		break
		
	else:		#tells the user if the command isn't valid
		print("\nThe command isn't valid. For a list of all commands, write 'instructions'")

	if end.unlocked:
		print("""\n    ----------
  
Congratulations! You've completed 'Strange House'.
To exit the game, press Enter

	----------""")

		input()
		break
	

	
	