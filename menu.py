import pygame, pygame_menu
import gamesettings
import start
""" creating menu using pygame_menu module parts are required for it to work """
pygame.init()
surface = pygame.display.set_mode(gamesettings.MENU_SIZE)
pygame.display.set_caption(gamesettings.MENU_MESSAGE)


def start_the_game(diff): # difficuly
	if diff == 0:
		start.set_the_game(diff)
		pygame.display.update()
	elif diff == 1:
		start.set_the_game(diff)
		pygame.display.update()
		print(1)
	else:
		start.set_the_game(diff)
		pygame.display.update()
		print(2)


def simulate_games():
	pass

menu = pygame_menu.Menu(gamesettings.MENU_MESSAGE, 900, 900, theme=pygame_menu.themes.THEME_DARK)


menu.add.button('Simulate 200 games (easy VS insane)', simulate_games)
menu.add.button('Play against human', start_the_game, diff=0, accept_kwargs=True)
menu.add.button('Play against easy AI', start_the_game, diff=1, accept_kwargs=True)
menu.add.button('Play against insane AI', start_the_game, diff=2, accept_kwargs=True)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

