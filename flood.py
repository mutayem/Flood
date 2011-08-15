import random
import board

up, right, down, left = range(4) 

def getup(row, col, colour, score):
	return getscore(row, col, colour, score, up)
def getright(row, col, colour, score):
	return getscore(row, col, colour, score, right)
def getdown(row, col, colour, score):
	return getscore(row, col, colour, score, down)
def getleft(row, col, colour, score):
	return getscore(row, col, colour, score, left)

def getscore(row, col, colour, score, direction):
	print "pos: ",row,"/",col,"   direction: ",direction,"  score: ",score

	# up
	if direction != down and row > 0:
		if b[row-1][col] == colour:
			score = score + getup(row-1, col, colour, score)
		else:
			score= score + 1

	# right
	if direction != left and col < 24:
		if b[row][col+1] == colour:
			score = score + getright(row, col + 1, colour, score)
		else:
			score = score+ 1

	print "pos: ",row,"/",col,"   direction: ",direction,"  score: ",score

	# down
	if direction != up and row < 24:
		if b[row+1][col] == colour:
			score = score + getdown(row+1, col, colour, score)
		else:
			score= score + 1

	print "pos: ",row,"/",col,"   direction: ",direction,"  score: ",score

	# left
	if direction != right and col > 0:
		if b[row][col-1] == colour:
			score = score + getleft(row, col-1, colour, score)
		else:
			score = score + 1

	print "pos: ",row,"/",col,"   direction: ",direction,"  score: ",score

	print "score: ", score
	return score


red, pink, blue, purple, yellow, green = range(6)

random.seed(2)
b = [[random.randint(0, 5) for col in range(25)] for row in range(25)] 

board.display(b)

colour = b[0][0]

getscore(0, 0, colour, 0, 999)


