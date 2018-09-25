import random
def holeone():
	onehole = input("\n\nHello there, you have arrived at the first tee!\n\nA short 152 yard par three easily reachable in one shot.\n\n Will you either \nA. Go over the bunker for a risky shot close to the hole with a 7 iron or \nB. Lay up with an 8 iron for a safer play? \n\nType A or B: \n\n ")
	while onehole != "A" or "B":
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		onehole = input("\n\n\n\nHello there, you have arrived at the first tee!\n\nA short 152 yard par three easily reachable in one shot.\n\n Will you either \nA. Go over the bunker for a risky shot close to the hole with a 7 iron or \nB. Lay up with an 8 iron for a safer play? \n\nType A or B: \n\n ")
		break
	if onehole == "A":
		distanceone = random.random()
