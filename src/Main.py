from Agent import Agent
from Maze import Maze
from Cell import Cell
from Position import Position
import pygame
import sys

# maze config
M_HEIGHT = 20
maze = Maze(M_HEIGHT)
maze.initialize()

agent = Agent(0, 0, maze)
path = agent.BFS(Position(19, 19))
print(path)
# setup window
FPS = 30
S_HEIGHT = 600
CELL_SIZE = S_HEIGHT // M_HEIGHT

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

# render the maze
def render_maze():
	x = 0
	y = 0
	for i in range(M_HEIGHT):
		for j in range(M_HEIGHT):
			cell = maze.get_value(i, j)
			if cell & Cell.UPWALL == 1:
				pygame.draw.line(screen, BLACK, [x, y], [x + CELL_SIZE, y])
			if cell & Cell.LEFTWALL == 8:
				pygame.draw.line(screen, BLACK, [x, y], [x, y + CELL_SIZE])
			if i == M_HEIGHT-1:
				if cell & Cell.RIGHTWALL == 2:
					pygame.draw.line(screen, BLACK, [x + CELL_SIZE, y], [x + CELL_SIZE, y + CELL_SIZE])
			if j == M_HEIGHT-1:
				if cell & Cell.DOWNWALL ==  4:
					pygame.draw.line(screen, BLACK, [x, y], [x, y + CELL_SIZE])
			y += CELL_SIZE
		y = 0
		x += CELL_SIZE
	
	pygame.display.update()


def traverse_maze():
	pass

render_maze()

# game loop
while True:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)