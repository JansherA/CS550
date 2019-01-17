#Monte Carlo Simulation
#Jansher Azmat
#Sources: 4 lines from Mrs. Healey's Monte Carlo Walk simulation: line 29, line 38, line 41, and line 42. Code commented out. 
#This is the first option of the Monte Carlo simulation. It tackles the issue of food waste and estimates the percent of food wasted for each person independent of their servings and calories per servings.
#Submitted Jan. 16 2019
#On my honor, I have neither given nor received unauthorized aid


import random #random amount of servings per person, calories per serving, and percent of food wasted per person
from collections import Counter #Helps to store the total amount of waste in a list, borrowed from Mrs. Healey's Monte Carlo simulation
import matplotlib.pyplot as plt #Plots the data

total_waste = [] #Creates list to store total amount of waste

for k in range(1000000): #Loops through the amount of trials, 1,000,000 takes a few seconds, but creates a more precise data set
	

	servings = random.randint(1,5) #The amount of servings an average person would eat during a single meal. I excluded the possibility of someone not eating in order to not skew data
	percent = 0 #This is the counter for the percent of food wasted
	for j in range(servings): #Loops through every serving
		calories = random.randint(50,500) #Picks random calorie amount for each serving
		amount = random.randint(1,99) #Picks random percent of aforementioned calorie amount for each serving
		percent = amount * calories / 100 #Operation to calculate the percent

	total_waste.append(percent) #Combines this percent with the total_waste list



results = sorted(Counter(total_waste).items()) #Sorts the data so it can be printed 

# print(results) #Optional line to print the results, would not recommend 


graph_data = [] #Creates list for each marker on the plot
x_data = [] #Creates list for each number on the x-axis, which is the amount of calories


for tuples in results: #Borrowed code from Mrs. Healey's Monte Carlo Simulation
	

	graph_data.append(tuples[1]) 
	x_data.append(tuples[0])



plt.style.use("dark_background") #This code makes the background of the plot black and it looks cool. Let's be honest here.

plt.plot(x_data,graph_data,"o",markersize=2, color = "cyan", fillstyle = "none")
		#Places the x-axis and y-axis numbers, as well as each marker
		#Each marker starts as a filled in circle, which is then reduced in size, changed to a cyan color, and turned into a hollow circle. Once again. It looks cool. 
plt.show() #Spits out the graph (ﾉ◕ヮ◕)ﾉ ᕙ(⇀‸↼‶)ᕗ



























