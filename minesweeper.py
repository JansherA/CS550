import random
import sys
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
def print_board(board):
	for i in board[1:-1]:
		print(*i[1:-1])
height = int(sys.argv[1])+2
width = int(sys.argv[2])+2
mines = int(sys.argv[3])
solution = [[0]*width for i in range(height)]
add_mines(solution)
print_board(solution)
# coordinate = str(input(bcolors.OKBLUE+"What point do you want to reveal?")).split(',')
print(*coordinate)
hi = [["∆"]*width for x in range(height)]


a = int(input("Height:")) + 1
b = int(input("Width:")) + 1
for x in range(height):
	for y in range(width):
		if board[a][b] == "*":
			hi[x][y] == board[x][y]
	
print(hi[a][b],end=" ")
