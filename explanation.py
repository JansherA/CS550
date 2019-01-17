#Explanation
#Jansher Azmat
#Sources: None
#This is the explanation for my option 1 Monte Carlo simulation, in code form. It teaches you everything about my simulation.
#Submitted Jan. 16 2019
#On my honor, I have neither given nor received unauthorized aid
def explain():
	print("\n\n Since we're in a computer science class, I figured the best way to present my code is via... code. I know, genius. (▰˘◡˘▰)\n\n")
	print("You have a few options on what to learn about first. \n\n A. What is the simulation about? \n\n B. How does it work? \n\n C. Why is this simulation important and relevent to Choate community members? \n\n D. Is this simulation accurate? \n\n E. Why is this simulation flawed in real life? \n\n F. How is it possible that Jansher is so awesome and deserves a 5? ╚(•⌂•)╝ ")
	question = input("\n\n What do you want to know about the simulation? Type a, b, c, d, e, or my personal favorite, f. All lowercase. Chop chop. No room for error here. \n\n Rerun your code after receiving an answer.\n\n")
	if question == "a":
		print("This simulation tackles the issue of how much food is wasted in the dining hall. Each point on the plot is a singular person's serving of food in calories and how much of it is wasted in percent. The x-axis is calories while the y-axis is the percent.")
	elif question == "b":
		print("The code is somewhat similar to my personal Monte Carlo walk simulation. It creates lists for the data and appends a number to said list once the number has gone through several calculations/randomizations. In this case, it loops through a million times for a good data set. A random amount amount of servings is assigned to the person. This is looped through and a random amount of calories and amount of food wasted is calculated. Then, all of these numbers go through an equation and turn into a percent that is appended to the list.")
	elif question == "c":
		print("\nBased on the simulation, although unrealistic in its own way, shows how much trash could be potentially produced. Students need to learn that taking less food each time (in this case, servings) is beneficial for the environment because it produces less trash. Rerun the code and select option E to see why the simulation inaccurately expresses this logic.")
	elif question == "d":
		print("\nIf you read through C, you can see (Very punny ôヮô) that it makes more sense to take less food in order to waste less. However, the data plotted on the chart created via the simulation is quite the opposite. In fact, the plot displayed shows that there is a very low percent percent of food wasted if a student were to attempt to consume 5 servings of 500 calories each. Rerun the code and select E to see why this is the case.")
	elif question == "e":
		print("\nBecause each randomization in my code is not weighted whatsoever, the data is skewed in an unrealistic way. For logistical reasons, I was unable to make it more likely to waste more food if the person has more food on their plate. The odds of a person wasting 99 percent of their food is the same regardless of whether they are attempting to consume 100 or 1000 calories.")
	elif question == "f":
		print("\nBeats me. (◠‿◠)")
	else: 
		print("\nYou had one job. (┛◉Д◉)┛彡┻━┻")
explain()
