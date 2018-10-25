#Minesweeper Game
#Jansher Azmat
#No Sources
#On my honor, I have neither given nor received unauthorized aid


import random
import sys


solution = [[] for x in range(0, boardsize+2)]
revealed = [[] for x in range(0, boardsize+2)]
for x in range(0, boardsize+2):
	solution[x] = [*]*(boardsize+2)
for x in range(0, boardsize+2):
	revealed[x] = [*]*(boardsize+2)
for x in range(1, boardsize+1):
for x in range(0, boardsize**2*0.2):
	solution[random.randrange(1,boardsize+1)][random.randrange(1,boardsize+1)] = 9
for x in range(0, boardsize):
	print(*solution[x])


for x in range(1,boardsize+1):


class bcolors:
	OKBLUE = '\033[94m'
	FAIL = '\033[91m'
print(bcolors.FAIL+"Minesweeper Board:")


def increase_around_bombs(r,c,board):
	for y in range(r-1, r+2):
		for x in range(c-1, c+2):
			if (board[y][x] is not "*"):
				board[y][x] += 1



def add_mines(board):
	for i in range(mines):
		x = random.randint(1,height-2)
		y = random.randint(1,width-2)
		while board[x][y] == '*':
			x = random.randint(1,height-2)
			y = random.randint(1,width-2)
		board[x][y] = '*'
		increase_around_bombs(x,y,board)


def print_board(board, hidden):
	for i in board[1:-1]:
		print(*i[1:-1])


height = int(sys.argv[1])+2
width = int(sys.argv[2])+2
mines = int(sys.argv[3])
solution = [[0]*width for i in range(height)]
hidden = [[1]*width for i in range(height)]
add_mines(solution)
print_board(solution, hidden)
finished = False
while finished == False:
	coordinate = str(input(bcolors.OKBLUE+"What point do you want to reveal?")).split(',')
	hidden[coordinate[0]][coordinate[1]] = 0
	if solution[coordinate[0]][coordinate[1]] == "*":
		print("You lost!")
		finished = True

#for i in solution():


#print(coordinate[0])

# a = coordinate[0]
# b = coordinate[1]
# for x in range(height):
# 	for y in range(width):
# 		if solution[a][b] == "*":
# 			hi[x][y] == solution[x][y]
	
# print(hi[a][b],end=" ")
