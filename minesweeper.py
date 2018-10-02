import random
import sys
row = int(sys.argv[1])
columns = int(sys.argv[2])
# 6 - 12 adapted from https://stackoverflow.com/questions/40566675/how-to-make-a-board-in-python most code adjusted because of required sys.argv
def board():
	print("Board:\n")

	for i in range(row): 
		x = [random.randrange(1, 3, 1) for _ in range(1)]
		print(*x * columns) 

if __name__ == '__main__':
	board()
