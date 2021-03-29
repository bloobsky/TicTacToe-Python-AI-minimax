""" Tic Tac Toe - Simple Game written in Python with use of xxx algorithm to work as an Artificial Intelligent player - that never loses.

Repository: https://www.github.com/bloobsky/tictactoe/
Documentation: https://www.github.com/bloobsky/tictactoe/README.md

"""
import pygame, sys, random, time
import numpy
# import local
import gamesettings

pygame.init() # required for pygame initialisation 



def create_lines(): # function that draw lines for the game
	""" 1st argument is linecolour 2nd args is where to start to draw 3rd when to finish the line and 4th is the line size """
	# horizontal lines
	pygame.draw.line(board, gamesettings.LINECOLOR, (0, 300), (900, 300), gamesettings.LINESIZE)
	pygame.draw.line(board, gamesettings.LINECOLOR, (0, 600), (900, 600), gamesettings.LINESIZE)
	# vertical lines
	pygame.draw.line(board, gamesettings.LINECOLOR, (300, 0), (300, 900), gamesettings.LINESIZE)
	pygame.draw.line(board, gamesettings.LINECOLOR, (600, 0), (600, 900), gamesettings.LINESIZE)

board = pygame.display.set_mode( (gamesettings.BOARDWIDTH, gamesettings.BOARDHEIGHT) )
board.fill( gamesettings.BOARDCOLOR )

backgroundBoard = numpy.zeros ( (gamesettings.BOARDROWS, gamesettings.BOARDCOLUMNS ) ) # populating 3x3 board with zeros 


def add_xo():
	for row in range(gamesettings.BOARDROWS):
		for column in range(gamesettings.BOARDCOLUMNS):
			if backgroundBoard[row][column] == 1:
				pygame.draw.circle( board, gamesettings.CIRCLE_COLOR, (int(column * 300 + 150), int(row * 300 + 150 )), gamesettings.CIRCLE_RADIUS, gamesettings.CIRCLE_SIZE)
			elif backgroundBoard[row][column] == 2:
				pygame.draw.line( board, gamesettings.HOURGLASS_COLOR, (column * 300 + gamesettings.HOURGLASS_SPACE, row * 300 + 300 - gamesettings.HOURGLASS_SPACE), (column * 300 + 300 - gamesettings.HOURGLASS_SPACE , row * 300 + gamesettings.HOURGLASS_SPACE), gamesettings.HOURGLASS_SIZE)
				pygame.draw.line( board, gamesettings.HOURGLASS_COLOR, (column * 300 + gamesettings.HOURGLASS_SPACE, row * 300 + gamesettings.HOURGLASS_SPACE), (column * 300 + 300 - gamesettings.HOURGLASS_SPACE , row * 300 + 300 - gamesettings.HOURGLASS_SPACE), gamesettings.HOURGLASS_SIZE)

def put_xo (row, column, player):
	""" rows, column and start from 0
	player options is 1 or 2 (we don't use 0 as it will not overwrite )
	 """
	backgroundBoard[row][column] = player


def available(row, column):
	""" function that checks if place is not already used """
	if backgroundBoard[row][column] == 0:
		return True
	else:
		return False

def no_more_moves():
	""" function which checks if the game is finished """
	for row in range(gamesettings.BOARDROWS):
		for column in range(gamesettings.BOARDCOLUMNS):
			if backgroundBoard[row][column] == 0: # args passed derived from for loops itself (row, column)
				return False
	return True

def check_win(player):
	# checking vertical line for win 
	for column in range(gamesettings.BOARDCOLUMNS):
		if backgroundBoard[0][column] == player and backgroundBoard[1][column] == player and backgroundBoard[2][column] == player:
			mark_vertical(column, player)
			return True
	# checking horizontal line for win
	for row in range(gamesettings.BOARDROWS):
		if backgroundBoard[row][0] == player and backgroundBoard[row][1] == player and backgroundBoard[row][2] == player:
			mark_horizontal(row, player)
			return True
	# checking cross line for win - top part
	if backgroundBoard[2][0] == player and backgroundBoard[1][1] == player and backgroundBoard[0][2] == player:
		mark_cross_top(player)
		return True

	# checking cross line for win - bottom part
	if backgroundBoard[0][0] == player and backgroundBoard[1][1] == player and backgroundBoard[2][2] == player:
		mark_cross_bottom(player)
		return True

	return False

def mark_horizontal(row, player):
	positionY = row * 300 + 150

	pygame.draw.line( board, gamesettings.WIN_COLOR, (15, positionY), (gamesettings.BOARDWIDTH - 15, positionY), 15)

def mark_vertical(column, player):
	positionX = column * 300 + 150
	pygame.draw.line( board, gamesettings.WIN_COLOR, (positionX, 15), (positionX, gamesettings.BOARDHEIGHT - 15), 15)

def mark_cross_top(player):
	pygame.draw.line( board, gamesettings.WIN_COLOR, (15, gamesettings.BOARDHEIGHT - 15), (gamesettings.BOARDWIDTH - 15, 15), 15)

def mark_cross_bottom(player):
	pygame.draw.line(board, gamesettings.WIN_COLOR, (15, 15), (gamesettings.BOARDWIDTH - 15, gamesettings.BOARDHEIGHT - 15), 15)

def reset_screen():
	board.fill(gamesettings.BOARDCOLOR)
	create_lines()
	for row in range(gamesettings.BOARDROWS):
		for column in range(gamesettings.BOARDCOLUMNS):
			backgroundBoard[row][column] = 0

def randomComputerMove():
	player = 2
	mademove = False
	# game_ends = False

	while not mademove:
		rowrandom = random.randrange(3)
		columnrandom = random.randrange(3)
		if available(rowrandom, columnrandom):
			put_xo(rowrandom, columnrandom, player)
			add_xo()
			mademove = True
			if check_win(player):
				game_ends = True
				mademove = True
				time.sleep(2)
				return game_ends
		else:
			mademove = False

def set_the_game(diff):
	reset_screen()
	# creating title for the window bar
	pygame.display.set_caption(gamesettings.GAMETITLE)
	game_ends = False
	player = 1
	
		
	if diff == 0:		# while Loop to keep the program running and will only exit when player close the game 
		while True:
			for action in pygame.event.get():
				if action.type == pygame.QUIT:
					sys.exit()

				if action.type == pygame.MOUSEBUTTONDOWN and not game_ends:

					clickX = action.pos[0] # x coordinate (horizontal)
					clickY = action.pos[1] # y coordinate (vertical)

					row_clicked = int(clickY // 300) # using divider 300 as screen is set to 900 so (1/3rd of the value) WARNING("DO NOT USE FLOAT as it will not work") 
					column_clicked = int(clickX // 300) # it simplifies the board to do low values (0,0 or 1,1) accordingly to the squares presented in 

					print(row_clicked)
					print(column_clicked)
					if available( row_clicked, column_clicked):
						put_xo( row_clicked, column_clicked, player)
						if check_win( player ):
							game_ends = True
							time.sleep(2)
						player = player % 2 + 1

						add_xo()

					print(backgroundBoard)
				
					if action.type == pygame.QUIT:
						sys.exit() 
								

			pygame.display.update() # required for board colouring
	elif diff == 1:
		while True:
			for action in pygame.event.get():
				player = 1
				if action.type == pygame.QUIT:
					sys.exit()

				if action.type == pygame.MOUSEBUTTONDOWN and not game_ends:

					clickX = action.pos[0] # x coordinate (horizontal)
					clickY = action.pos[1] # y coordinate (vertical)

					row_clicked = int(clickY // 300) # using divider 300 as screen is set to 900 so (1/3rd of the value) WARNING("DO NOT USE FLOAT as it will not work") 
					column_clicked = int(clickX // 300) # it simplifies the board to do low values (0,0 or 1,1) accordingly to the squares presented in 

					print(row_clicked)
					print(column_clicked)
					if available( row_clicked, column_clicked):
						put_xo( row_clicked, column_clicked, player)
						add_xo()
						if check_win( player ):
							game_ends = True
							print('finish')
						
					if not game_ends:
						randomComputerMove()

					

					print(backgroundBoard)
				
					if action.type == pygame.QUIT:
						sys.exit() 
								

			pygame.display.update() # required for board colouring
	elif diff == 2:
		print(2)
		while True:
			for action in pygame.event.get():
				player = 1
				if action.type == pygame.QUIT:
					sys.exit()

				if action.type == pygame.MOUSEBUTTONDOWN and not game_ends:

					clickX = action.pos[0] # x coordinate (horizontal)
					clickY = action.pos[1] # y coordinate (vertical)

					row_clicked = int(clickY // 300) # using divider 300 as screen is set to 900 so (1/3rd of the value) WARNING("DO NOT USE FLOAT as it will not work") 
					column_clicked = int(clickX // 300) # it simplifies the board to do low values (0,0 or 1,1) accordingly to the squares presented in 

					print(row_clicked)
					print(column_clicked)
					if available( row_clicked, column_clicked):
						put_xo( row_clicked, column_clicked, player)
						add_xo()
						if check_win( player ):
							game_ends = True
							print('finish')
							return game_ends

						randomComputerMove()
					

					print(backgroundBoard)
				
					if action.type == pygame.QUIT:
						sys.exit() 
								

			pygame.display.update() # required for board colouring
	else:
		print('Ai not available')		