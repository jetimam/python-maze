from Agent import Agent
from Maze import Maze
from Cell import Cell
from Position import Position
import pygame
import sys

# maze config
M_HEIGHT = 5
maze = Maze(M_HEIGHT)
maze.initialize()

# setup window
FPS = 30
S_HEIGHT = 800
CELL_SIZE = S_HEIGHT // M_HEIGHT

# agent config
agent = Agent(Position(0, 0), maze)
A_SIZE = CELL_SIZE // 4

# manual user config
user_pos = Position((CELL_SIZE/2), (CELL_SIZE/2))

# colors
WHITE = (255, 255, 255)
BLACK  = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 225)

# pygame init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((S_HEIGHT, S_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Python Maze")
clock = pygame.time.Clock()

def render_maze():
	x = 0
	y = 0
	for i in range(M_HEIGHT):
		for j in range(M_HEIGHT):
			cell = maze.get_value(i, j)
			if cell & Cell.UPWALL == 1:
				pygame.draw.line(screen, BLACK, [x, y], [x + CELL_SIZE, y])
			if cell & Cell.RIGHTWALL == 2:
				pygame.draw.line(screen, BLACK, [x + CELL_SIZE, y], [x + CELL_SIZE, y + CELL_SIZE])
			if cell & Cell.DOWNWALL ==  4:
				pygame.draw.line(screen, BLACK, [x, y + CELL_SIZE], [x + CELL_SIZE, y + CELL_SIZE])
			if cell & Cell.LEFTWALL == 8:
				pygame.draw.line(screen, BLACK, [x, y], [x, y + CELL_SIZE])
			y += CELL_SIZE
		y = 0
		x += CELL_SIZE
	
	pygame.display.update()

def render_user():
	pygame.draw.circle(screen, BLUE, [user_pos.x, user_pos.y], A_SIZE)
	pygame.display.update()

def move_up():
	pygame.draw.circle(screen, WHITE, [user_pos.x, user_pos.y], A_SIZE)
	user_pos.y = user_pos.y - CELL_SIZE
	pygame.draw.circle(screen, BLUE, [user_pos.x, user_pos.y], A_SIZE)
	pygame.display.update()

def move_left():
	pygame.draw.circle(screen, WHITE, [user_pos.x, user_pos.y], A_SIZE)
	user_pos.x = user_pos.x - CELL_SIZE
	pygame.draw.circle(screen, BLUE, [user_pos.x, user_pos.y], A_SIZE)
	pygame.display.update()

def move_down():
	pygame.draw.circle(screen, WHITE, [user_pos.x, user_pos.y], A_SIZE)
	user_pos.y = user_pos.y + CELL_SIZE
	pygame.draw.circle(screen, BLUE, [user_pos.x, user_pos.y], A_SIZE)
	pygame.display.update()

def move_right():
	pygame.draw.circle(screen, WHITE, [user_pos.x, user_pos.y], A_SIZE)
	user_pos.x = user_pos.x + CELL_SIZE
	pygame.draw.circle(screen, BLUE, [user_pos.x, user_pos.y], A_SIZE)
	pygame.display.update()

# game
render_maze()
render_user()

while True:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				move_up()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				move_left()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				move_down()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				move_right()