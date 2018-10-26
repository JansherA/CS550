class Bank:
	def __init__(self, name, pin, money):
		self.name = name
		self.pin = pin
		self.money = money
	nameone = input("\n What is your name? ")
	number = input("\n Choose a pin: \n\n ")
	def deposit(self):
		status = ""
		enter = input("\n\nEnter your pin: \n\n")
		if enter == number:
			if self.money < 100000:
				self.money += add
				status = "\n You successfully deposited money. Here is your new total: \n"+self.money
			else: 
				status = "\n You are unable to deposit! Here is your balance: \n"+self.money
			return status
	def statement(self):
		return self.name+" , your total balance is" +str(self.money)
one = Bank(name, pin, money)
	#deposit(self)



while True:
	print(first.stats())
	choice = input("What do you want to do?")
	if choice == "Deposit" or "deposit":
		print(one.deposit())
	# elif choice == "sleep":
	# 	first.sleep()
	else:
		print("Can't do that. ")
