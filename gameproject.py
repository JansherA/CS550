import random
def holeone():
	onehole = input("\n\nHello there, you have arrived at the first tee!\n\nA short 152 yard par three easily reachable in one shot.\n\n Will you either \nA. Go over the bunker for a risky shot close to the hole with a 7 iron or \nB. Lay up with an 8 iron for a safer play? \n\nType A or B: \n\n ")
	while onehole != "A" or "B":
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		onehole = input("\n\n\n\nHello there, you have arrived at the first tee!\n\nA short 152 yard par three easily reachable in one shot.\n\n Will you either \nA. Go over the bunker for a risky shot close to the hole with a 7 iron or \nB. Lay up with an 8 iron for a safer play? \n\nType A or B: \n\n ")
		break
	if onehole == "A":
		distanceone = random.random()
		if distanceone < .25:
			print("Success! You are within 5 feet for an easy putt. Nice birdie.")
			holetwo()
		else:
			holeoneshottwo = input("\n\nOops...Your ball landed in the bunker. \n\nWill you \nA. Forfeit the hole and save your energy for an automatic score of 10 on the hole or \n\nB. Continue for a chance of an 5? Type A or B: \n\n ")
			while holeoneshottwo != "A" or "B":
				print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
				holeoneshottwo = input("\n\nOops...Your ball landed in the bunker. \n\nWill you \nA. Forfeit the hole and save your energy for an automatic score of 10 on the hole or \n\nB. Continue for a chance of an 5? Type A or B: \n\n ")
				break
			if holeoneshottwo == "B":
				distancetwo = random.random()
				if distancetwo < .25:
					print("Good job! You nailed the putt and recovery. At least you scored a 5 and saved yourself from disaster.")
					holetwo()
				else:
					print("Unlucky! You still managed to score a 10 with that horrible recovery from the sand. Might as well have forfeited the hole.")
					holetwo()
			elif holeoneshottwo == "A":
				print("Horrible idea! Why would you conserve your energy? This is golf, not cross country. Drink a redbull and take your score of 10.")
				holetwo()
	elif onehole == "B":
		print("Smart play! You mitigated the risks and secured an easy par 3 without breaking a sweat. However, that also makes you lame.")		
		holetwo()
