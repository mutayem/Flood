import random
import board

up, right, down, left = range(4) 

def getup(row, col, colour):
	return getscore(row, col, colour, up)
def getright(row, col, colour):
	return getscore(row, col, colour, right)
def getdown(row, col, colour):
	return getscore(row, col, colour, down)
def getleft(row, col, colour):
	return getscore(row, col, colour, left)

def getscore(row, col, colour, direction):
	score = 0

	# right
	if direction != left and col < 24:
		if b[row][col+1] == colour:
			score = score + getright(row, col + 1, colour)
		else:
			score = score+ 1

	# left
	if direction != right and col > 0:
		if b[row][col-1] == colour:
			score = score + getleft(row, col-1, colour)
		else:
			score= score + 1

	# up
	if direction != down and row > 0:
		if b[row+1][col] == colour:
			score = score + getup(row+1, col, colour)
		else:
			score= score + 1

	# down
	if direction != up and col < 24:
		if b[row-1][col] == colour:
			score = score + getdown(row-1, col, colour)
		else:
			score= score + 1

	print "score: ", score

	return score


red, pink, blue, purple, yellow, green = range(6)

random.seed(2)
b = [[random.randint(0, 5) for col in range(25)] for row in range(25)] 

board.display(b)

colour = b[0][0]

getscore(0, 0, colour, 999)


