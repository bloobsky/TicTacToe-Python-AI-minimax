""" 
	constants and variables used for the tic tac toe game 
    colours for the game should be present in RGB format (x, x ,x   )
"""

# Board settings (visible part)
BOARDWIDTH = 900 # setting board size in pixels
BOARDHEIGHT = 900
GAMETITLE = "Tic Tac Toe by Mattie Jakusz" # in window title 
BOARDCOLOR = (0, 0, 0) # black
LINECOLOR = (192, 192, 192) # silver
LINESIZE = 4 # use even number when possible for better board reading

# signs X(hourglass) O(circle) settings
HOURGLASS_COLOR = (102, 0, 0) # red
HOURGLASS_SIZE = 10 
HOURGLASS_SPACE = 50
CIRCLE_COLOR = (0, 102, 0) # green
CIRCLE_RADIUS = 90
CIRCLE_SIZE = 10
WIN_COLOR = (255, 255, 255) #white


# background board settings (concealed part) [3x3]
BOARDROWS = 3
BOARDCOLUMNS = 3

# Main Menu
# to change a theme go to pygame_menu docs

MENU_SIZE = (900, 900) # try use the samevalues as for board width and height
MENU_MESSAGE = "MAIN MENU / Tic Tac Toe by Mattie Jakusz"