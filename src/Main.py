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

# setup window
FPS = 30
S_HEIGHT = 800
CELL_SIZE = S_HEIGHT // M_HEIGHT

# agent config
agent = Agent(Position(M_HEIGHT-1, M_HEIGHT-1), maze)
A_SIZE = CELL_SIZE // 4

# manual user config
user_pos = Position(0, 0)

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

def translate_coordinates(maze_position):
	return (maze_position+0.5) * (CELL_SIZE)

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

def render_agent():
	pygame.draw.circle(screen, RED, [translate_coordinates(agent.position.x), translate_coordinates(agent.position.y)], A_SIZE)
	pygame.display.update()

def render_user():
	pygame.draw.circle(screen, BLUE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def can_move(direction):
	if direction == 'up':
		cell = maze.get_value(user_pos.x, user_pos.y)
		return cell & Cell.UPWALL != 1
	elif direction == 'right':
		cell = maze.get_value(user_pos.x, user_pos.y)
		return cell & Cell.RIGHTWALL != 2
	elif direction == 'down':
		cell = maze.get_value(user_pos.x, user_pos.y)
		return cell & Cell.DOWNWALL != 4
	elif direction == 'left':
		cell = maze.get_value(user_pos.x, user_pos.y)
		return cell & Cell.LEFTWALL != 8

def move_up():
	pygame.draw.circle(screen, WHITE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.y = user_pos.y - 1
	pygame.draw.circle(screen, BLUE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def move_left():
	pygame.draw.circle(screen, WHITE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.x = user_pos.x - 1
	pygame.draw.circle(screen, BLUE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def move_down():
	pygame.draw.circle(screen, WHITE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.y = user_pos.y + 1
	pygame.draw.circle(screen, BLUE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def move_right():
	pygame.draw.circle(screen, WHITE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.x = user_pos.x + 1
	pygame.draw.circle(screen, BLUE, [translate_coordinates(user_pos.x), translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def ai_traversal():
	path = agent.search_BFS(user_pos)
	pygame.draw.circle(screen, WHITE, [translate_coordinates(agent.position.x), translate_coordinates(agent.position.y)], A_SIZE)
	agent.position = path[1]
	pygame.draw.circle(screen, RED, [translate_coordinates(agent.position.x), translate_coordinates(agent.position.y)], A_SIZE)
	pygame.display.update()

# game
render_maze()
render_agent()
render_user()

while True:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if user_pos == agent.position:
			pygame.quit()
			print('GG')
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_w and can_move('up'):
				move_up()
			elif event.key == pygame.K_a and can_move('left'):
				move_left()
			elif event.key == pygame.K_s and can_move('down'):
				move_down()
			elif event.key == pygame.K_d and can_move('right'):
				move_right()
			else:
				continue
			ai_traversal()