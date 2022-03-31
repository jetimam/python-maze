from Agent import Agent
from Maze import Maze
from Cell import Cell
from Position import Position
import Util
import pygame
import sys
import math

# maze config
maze = Maze(Util.M_HEIGHT)
maze.initialize()

# agent config
agent = Agent(Position(Util.M_HEIGHT-1, Util.M_HEIGHT-1), maze)
A_SIZE = Util.CELL_SIZE // 4

# manual user config
user_pos = Position(0, 0)

# pygame init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Util.S_HEIGHT, Util.S_HEIGHT))
screen.fill(Util.WHITE)
pygame.display.set_caption("Python Maze")
clock = pygame.time.Clock()

def render_maze():
	x = 0
	y = 0
	for i in range(Util.M_HEIGHT):
		for j in range(Util.M_HEIGHT):
			cell = maze.get_value(i, j)
			if cell & Cell.UPWALL == 1:
				pygame.draw.line(screen, Util.BLACK, [x, y], [x + Util.CELL_SIZE, y])
			if cell & Cell.RIGHTWALL == 2:
				pygame.draw.line(screen, Util.BLACK, [x + Util.CELL_SIZE, y], [x + Util.CELL_SIZE, y + Util.CELL_SIZE])
			if cell & Cell.DOWNWALL ==  4:
				pygame.draw.line(screen, Util.BLACK, [x, y + Util.CELL_SIZE], [x + Util.CELL_SIZE, y + Util.CELL_SIZE])
			if cell & Cell.LEFTWALL == 8:
				pygame.draw.line(screen, Util.BLACK, [x, y], [x, y + Util.CELL_SIZE])
			y += Util.CELL_SIZE
		y = 0
		x += Util.CELL_SIZE
	
	pygame.display.update()

def debug_viz(path):
	pass

def render_agent():
	pygame.draw.circle(screen, Util.RED, [Util.translate_coordinates(agent.position.x), Util.translate_coordinates(agent.position.y)], A_SIZE)
	pygame.display.update()

def render_user():
	pygame.draw.circle(screen, Util.BLUE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
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
	pygame.draw.circle(screen, Util.WHITE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.y = user_pos.y - 1
	pygame.draw.circle(screen, Util.BLUE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def move_left():
	pygame.draw.circle(screen, Util.WHITE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.x = user_pos.x - 1
	pygame.draw.circle(screen, Util.BLUE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def move_down():
	pygame.draw.circle(screen, Util.WHITE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.y = user_pos.y + 1
	pygame.draw.circle(screen, Util.BLUE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def move_right():
	pygame.draw.circle(screen, Util.WHITE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	user_pos.x = user_pos.x + 1
	pygame.draw.circle(screen, Util.BLUE, [Util.translate_coordinates(user_pos.x), Util.translate_coordinates(user_pos.y)], A_SIZE)
	pygame.display.update()

def ai_traversal():
	euclidean = lambda x,y,x_t,y_t: math.sqrt((x_t - x)**2 + (y_t - y)**2)
	manhattan = lambda x, y, x_t, y_t: abs(x - x_t) + abs(y - y_t)
	# path = agent.search_BFS(user_pos, False, screen)
	path = agent.search_AS(user_pos, manhattan, False, screen)
	pygame.draw.circle(screen, Util.WHITE, [Util.translate_coordinates(agent.position.x), Util.translate_coordinates(agent.position.y)], A_SIZE)
	agent.position = path[1]
	pygame.draw.circle(screen, Util.RED, [Util.translate_coordinates(agent.position.x), Util.translate_coordinates(agent.position.y)], A_SIZE)
	pygame.display.update()

def debug(type):
	render_maze()
	while True:
		clock.tick(Util.FPS)
		if type == "bfs":
			agent.search_BFS(user_pos, True, screen)
			type = 'used'
		elif type == "as_euclidean":
			euclidean = lambda x,y,x_t,y_t: math.sqrt((x_t - x)**2 + (y_t - y)**2)
			agent.search_AS(user_pos, euclidean, True, screen)
			type = 'used'
		elif type == "as_manhattan":
			manhattan = lambda x, y, x_t, y_t: abs(x - x_t) + abs(y - y_t)
			agent.search_AS(user_pos, manhattan, True, screen)
			type = 'used'
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

def game():
	render_maze()
	render_agent()
	render_user()

	while True:
		clock.tick(Util.FPS)
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

game()
# debug("bfs")