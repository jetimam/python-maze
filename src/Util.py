import pygame

M_HEIGHT = 25
FPS_GAME = 5
FPS_DEBUG = 30
S_HEIGHT = 800
CELL_SIZE = S_HEIGHT // M_HEIGHT

# colors
WHITE = (255, 255, 255)
BLACK  = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 225)
PURPLE = (255, 0, 255)

def translate_coordinates(position):
	return (position+0.5) * (CELL_SIZE)
def draw_rect_debug(screen, color, position):
	x = translate_coordinates(position.x)
	y = translate_coordinates(position.y)
	pygame.draw.rect(screen, color, pygame.Rect(x, y, CELL_SIZE/2, CELL_SIZE/2))
	pygame.display.update()
	pygame.event.get()
	# pygame.time.wait(50)