from time import sleep
from Cell import Cell
from random import randint
import numpy

class Maze:
	def __init__(self, height, width):
		self.height = height
		self.width = width
	
	def initialize(self):
		maze = []
		initial = Cell.UPWALL | Cell.RIGHTWALL | Cell.DOWNWALL | Cell.LEFTWALL
		for i in range(self.height-1): # y
			maze.append([])
			for j in range(self.width-1): # x
				maze[i].append(initial)

		return self.DFS(maze)

	def DFS(self, maze):
		stack = []
		x = 0
		y = 0
		stack.append([maze[x][y], x, y]) # not my proudest design

		while(len(stack) > 0):
			current_cell = stack.pop()
			sleep(1)
			print(current_cell[1],current_cell[2])
			current_cell[0] |= Cell.VISITED
			children = self.generate_random_child(current_cell, maze)
			if len(children) > 0:
				stack.append(current_cell) # so that the other children can be explored when we eventually backtrack
				random_child = children[randint(0, len(children)-1)]
				unit_v = numpy.subtract((random_child[1], random_child[2]), (current_cell[1], current_cell[2])) # indicates the direction from current->child

				if unit_v[0] == 1: # right
					current_cell[0] &= Cell.RIGHTWALL
					random_child[0] &= Cell.LEFTWALL
				if unit_v[0] == -1: #left
					current_cell[0] &= Cell.LEFTWALL
					random_child[0] &= Cell.RIGHTWALL
				if unit_v[1] == 1: #up
					current_cell[0] &= Cell.UPWALL
					random_child[0] &= Cell.DOWNWALL
				if unit_v[1] == -1: #down
					current_cell[0] &= Cell.DOWNWALL
					random_child[0] &= Cell.UPWALL

				stack.append(random_child)

		return maze

	def generate_random_child(self, parent_cell, maze):
		children = []
		x = parent_cell[1]
		y = parent_cell[2]

		if x > 0: #left border
			if maze[x-1][y] & Cell.VISITED == 0:
				children.append([maze[x-1][y], x-1, y])
		if y > 0: #up border
			if maze[x][y-1] & Cell.VISITED == 0:
				children.append([maze[x][y-1], x, y-1])
		if x < self.width-2: #right border
			if maze[x+1][y] & Cell.VISITED == 0:
				children.append([maze[x+1][y], x+1, y])
		if y < self.height-2: #down border
			print('in if')
			if maze[x][y+1] & Cell.VISITED == 0:
				children.append([maze[x][y+1], x, y+1])

		return children