import board

masterBoard = [['r' for col in range(25)] for row in range(25)] 

board.display(masterBoard)

start(0, 0)


def start(row, col):
	print row, col
