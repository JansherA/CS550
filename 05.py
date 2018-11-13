class Koala:

	# energy 10 = low 100 = high
	#hunger 10 = low 100 = high



	#constructor
	#initializes properties and sets up the dog object
	#1-100 Scale Inclusive
	def __init__(self, name, hunger, energy, owner):
		self.hunger = hunger
		self.energy = energy
		self.name = name
		self.owner = owner
	#methods/functions
	def eat(self):
		status = ""
		if self.hunger > 0 and self.energy < 100:
			self.hunger -= 40
			self.energy += 30
			status = self.name+"\n You just ate!"
		else:
			status = self.name+"\n Too tired or full to eat!"
		return status
	def sleep(self):
		if self.hunger > 0 and self.energy < 100:
			self.energy += 70
			self.hunger += 10
			status = self.name+"\n You just slept!"
		else:
			status = self.name+"\n Too tired or full to sleep!"
		return status
	def stats(self):
		return "Name: "+self.name+"\nEnergy: "+str(self.energy)+"\nHunger: "+str(self.hunger)


own = input("What is your name? ")
first = Koala("Kiko" , 70, 20, own)
second = Koala("Kato" , 60, 10, own)


while True:
	print(first.stats())
	print(second.stats())
	choice = input("What do you want to do?")
	if choice == "eat":
		print(first.eat())
		print(second.eat())
	elif choice == "sleep":
		first.sleep()
		second.sleep()
	else:
		print("Can't do that. ")