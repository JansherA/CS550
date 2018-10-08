import random
import sys
class bcolors:
	OKBLUE = '\033[94m'
	FAIL = '\033[91m'
row = int(sys.argv[1]) + 2
columns = int(sys.argv[2]) + 2
bombs = int(sys.argv[3])
myboard = [[0]*columns for i in range(row)]
def board():
	print(bcolors.FAIL+"Minesweeper Board: \n")
	# print(*myboard, sep='\n')
for i in range(bombs):
	down = random.randint(1,row-2)
	over = random.randrange(1,columns-2)
	while myboard[down][over] is "*":
		myboard = [[0]*columns for i in range(row)]
	myboard[down][over] = "*"
	if myboard[down][over-1] is not "*":
		myboard[down][over-1] += 1
	if myboard[down][over+1] is not "*":
		myboard[down][over+1] += 1
	if myboard[down-1][over] is not "*":
		myboard[down-1][over] += 1
	if myboard[down+1][over] is not "*":
		myboard[down+1][over] += 1
	if myboard[down-1][over-1] is not "*":
		myboard[down-1][over-1] += 1
	if myboard[down-1][over+1] is not "*":
		myboard[down-1][over+1] += 1
	if myboard[down+1][over+1] is not "*":
		myboard[down+1][over+1] += 1
	if myboard[down+1][over-1] is not "*":
		myboard[down+1][over-1] += 1
if __name__ == '__main__':
	board()
for j in myboard[1:-1]:
	print(*j[1:-1])
