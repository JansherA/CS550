#Jansher Azmat 9-20-18
#I have neither given nor received unauthorized aid

#Golf round! University of Oklahoma's 4 hole golf course with your choice of shot selection and decisions
import random
def holeone():
	#This is the function for the first hole
	onehole = input("\n\nHello there, you have arrived at the first tee!\n\nA short 152 yard par three easily reachable in one shot.\n\n Will you either \nA. Go over the bunker for a risky shot close to the hole with a 7 iron or \nB. Lay up with an 8 iron for a safer play? \n\nType A or B: \n\n ")
	while onehole != "A" or "B":
#CRHMHEALEY Github Demo While Loop
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		onehole = input("\n\n\n\nHello there, you have arrived at the first tee!\n\nA short 152 yard par three easily reachable in one shot.\n\n Will you either \nA. Go over the bunker for a risky shot close to the hole with a 7 iron or \nB. Lay up with an 8 iron for a safer play? \n\nType A or B: \n\n ")
		break
	if onehole == "A":
		distanceone = random.random()
		#The point of this variable is to incorporate probability into the user's decision
		#First day progress ^
		if distanceone < .25:
			#As you can see, there is a low 25% chance that the user selects a risky option and it turns out to be true
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
				#Once again, I used probability here so that the user has to use strategy
				if distancetwo < .25:
					print("Good job! You nailed the putt and recovery. At least you scored a 5 and saved yourself from disaster.")
					holetwo()
				else:
					print("Unlucky! You still managed to score a 10 with that horrible recovery from the sand. Might as well have forfeited the hole.")
					holetwo()
			elif holeoneshottwo == "A":
				print("Horrible idea! Why would you conserve your energy? This is golf, not cross country. Drink a redbull and take your score of 10.")
				holetwo()
				#Here I'm calling the next hole's function before it is created to advance my code after the user is finished with this hole
	elif onehole == "B":
		print("Smart play! You mitigated the risks and secured an easy par 3 without breaking a sweat. However, that also makes you lame.")		
		holetwo()
#First day homework ^
def holetwo():
	#This is the function for the second hole
	twohole = input("\n\n\n\nCongrats, you've made it to the second hole.\n\nHere we have a far longer par 5 - about 542 yards with a dogleg left. \n\n Will you either \n\nA. Pull out your driver and go over the water 300 yards out or \n\nB. Land the ball just short of the hazard with a 3 wood for a much safer shot? \n\nType A or B: \n\n ")
	#I used several indentations and tabs in my print statements to clearly indicate to the user what I am attempting to say and make the options easy to read
	while twohole != "A" or "B":
		#This loop is for error checking, the only two options allowed in my input are A and B - anything else is disregarded by this loop
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		twohole = input("\n\n\n\nCongrats, you've made it to the second hole.\n\nHere we have a far longer par 5 - about 542 yards with a dogleg left. \n\n Will you either \n\nA. Pull out your driver and go over the water 300 yards out or \n\nB. Land the ball just short of the hazard with a 3 wood for a much safer shot? \n\nType A or B: \n\n ")
		break
	if twohole == "A":
		holetwoshotone = random.random()
		if holetwoshotone < .25:
			print("Excellent shot! You crushed that drive and completely cleared the water, an easy setup for a score of 3. Nice eagle! ")
#Extra Help Progress ^
			holethree()
		else:
			holetwoshottwo = input("Ouch! You failed to clear the water. After dropping your ball, the two options are to \n\nA. Lay up again to the green for a good chance of a 5 or \n\nB. Go for it again for a low chance of a 4. ")
			while holeoneshottwo != "A" or "B":
				print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
				holetwoshottwo = input("Ouch! You failed to clear the water and instead have a penalty of +2. After dropping your ball, the two options are to \n\nA. Lay up again to the green for a good chance of a 5 or \n\nB. Go for it again for a low chance of a 4. ")
				break
				#Here I have to break the loop in order to stop it from running forever and continually asking for input
			if holetwoshottwo == "A":
				number = random.random()
				if number > .5:
					print("You landed the ball 100 yards from the green. Nice job! Now you have an easy pitch shot and up and down to save par. Nice 5! ")
					holethree()
				else:
					print("Unlucky! You failed to layup and your ball is now in the rough. Your score for this hole is 6.")
					holethree()
			elif holetwoshottwo == "B":
				hello = random.random()
				if hello > .25:
					print("You are a couple feet away from the green. Great shot! Your score from this hole is a 4 after that easy up-and-down ")
					holethree()
				else: 
					print("Bummer! You chunked that shot and barely made progress. A smooth up-and-down and your score is a 6. Not bad! ")
					holethree()
	elif twohole == "B":
		#In golf, laying up is a high probability shot that is highly likely
		#As a result, I don't need to have a probability statement if the odds are 90%+
		print("Smart play! You eliminated any risks with the guaranteed shot and put yourself in an easy position for a 5. Nice par! ")
		holethree()
def holethree():
	threehole = input("\n\nNice job so far. You've made it to hole number three which is a longer 210 yard par three. Be careful of the large greenside bunker on this one! Your two options are to \n\nA. Hit a hybrid straight over the bunker for a chance at birdie or \n\nB. Lay up to the sand for a guaranteed par. \n\nType A or B: \n\n ")
	while threehole != "A" or "B":
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		threehole = input("\n\nNice job so far. You've made it to hole number three which is a longer 210 yard par three. Be careful of the large greenside bunker on this one! Your two options are to \n\nA. Hit a hybrid straight over the bunker for a chance at birdie or \n\nB. Lay up to the sand for a guaranteed par. \n\nType A or B: \n\n ")
		break
	if threehole == "A":
		choate = random.random()
		#Eventually I started using random variable names since my if's are organized
		if choate >.1:
			print("Wow! Excellent shot. You are inches from the pin with a tap in birdie. Nice 3! ")
			holefour()
		else:
			print("That's unfortunate. You are way off to the right and in the thick rough. Take your 4 and leave. ")
			holefour()
	elif threehole == "B":
		print("Your I.Q. is off the charts. You made an easy par by laying up to the bunker and having to deal with a long putt instead. Easy score of 3! ")
		holefour()
		#I'm calling the function before it is created
def holefour():
	#Now I'm finally defining the function
	fourhole = input("\n\nYou aren't doing as bad as I suspected. This hole will turn that around. A medium par 4 with several obstacles. No easy way out this time! Your two options from the tee are \n\nA. Hit a draw around the tree for a good set up or \n\nB. Hit a fade to the other side of the fairway for a longer yet straighter second shot. \n\nType A or B: \n\n ")
	while fourhole != "A" or "B":
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		fourhole = input("\n\nYou aren't doing as bad as I suspected. This hole will turn that around. A medium par 4 with several obstacles. No easy way out this time! Your two options from the tee are \n\nA. Hit a draw around the tree for a good set up or B. Hit a fade to the other side of the fairway for a longer yet straighter second shot. \n\nType A or B: \n\n ")
		break
	if fourhole == "A":
		thisishard = random.random()
		if thisishard > .5:
			rosemary = input("Nice shot shape! You curved around that tree perfectly. Take your par and head on over to the clubhouse. ")
			clubhouse()
		else:
			print("That ought to hurt. You rammed directly into a branch. Your ball bounced back 50 yards, but at least you have a straight shot at the hole. A well earned score of 5. ")
	elif fourhole == "B":
		whynot = random.random()
		if whynot > .5:
			print("What a shot! You faded the ball pefectly and have an easy par. Go onwards to the clubhouse with your 4 on this hole. ")
			clubhouse()
		else:
			print("Good try, I guess. Your ball fell into a ditch, leaving you with a bogey to end it off. Head to the clubhouse with a 5 on this hole. ")
			clubhouse()
def clubhouse():
	#This function is just for fun, it wraps the round up with humour
	almostdone = input("That was a nice round! Would you like anything to drink before you leave? Choose \n\nA. Coke or \n\nB. Pepsi. \n\nType A or B. \n\n")
	while almostdone != "A" or "B":
		print("You didn't type A or B! (Mrs. Healey stop it I need a good grade) Try again please.")
		almostdone = input("That was a nice round! Would you like anything to drink before you leave? Choose \n\nA. Coke or \n\nB. Pepsi. \n\nType A or B. \n\n")
		break
	if almostdone == "A":
		print("Good choice. That'll be $4. Goodbye!")
	elif almostdone == "B":
		print("That was a joke. No one likes Pepsi. Your coke will be $4. Adios!")

#And alas, I'm calling the initial function to execute. I don't need to call the other ones since they naturally are called after each option
holeone()


