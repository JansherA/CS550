import random
import sys

boardsize = 16

solution = [[] for x in range(0, boardsize+2)]
revealed = [[] for x in range(0, boardsize+2)]
for x in range(0, boardsize+2):
	solution[x] = ["*"]*(boardsize+2)
for x in range(0, boardsize+2):
	revealed[x] = ["*"]*(boardsize+2)
for x in range(0, int(boardsize**2*0.2)):
	solution[random.randrange(1,boardsize+1)][random.randrange(1,boardsize+1)] = 9
for x in range(0, boardsize):
	print(*solution[x])

for x in range(1,boardsize+1):
	for y in range(1,boardsize+1)