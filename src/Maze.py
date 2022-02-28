from time import sleep
from Cell import Cell
from random import randint
import numpy

class Maze:
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.maze = []
	
	def initialize(self):
		initial = Cell.UPWALL | Cell.RIGHTWALL | Cell.DOWNWALL | Cell.LEFTWALL
		for i in range(self.height-1): # y
			self.maze.append([])
			for j in range(self.width-1): # x
				self.maze[i].append(initial)

		return self.DFS()

	def DFS(self):
		stack = []
		x = 0
		y = 0
		stack.append([x, y])
		while(len(stack) > 0):
			current_cell = stack.pop()
			self.maze[current_cell[0]][current_cell[1]] |= Cell.VISITED
			sleep(1)
			children = self.generate_random_child(current_cell)
			if len(children) > 0:
				stack.append(current_cell) # so that the other children can be explored when we eventually backtrack
				random_child = children[randint(0, len(children)-1)]
				unit_v = numpy.subtract((random_child[0], random_child[1]), (current_cell[0], current_cell[1])) # indicates the direction from current->child
				self.remove_common_wall(current_cell, random_child, unit_v)
				stack.append(random_child)

		return self.maze

	def generate_random_child(self, parent_cell):
		children = []
		x = parent_cell[0]
		y = parent_cell[1]
		print('current cell:', x, y)

		if x > 0: #left border
			if self.maze[x-1][y] & Cell.VISITED == 0:
				children.append([x-1, y])
		if y > 0: #up border
			if self.maze[x][y-1] & Cell.VISITED == 0:
				children.append([x, y-1])
		if x < self.width-2: #right border
			if self.maze[x+1][y] & Cell.VISITED == 0:
				children.append([x+1, y])
		if y < self.height-2: #down border
			if self.maze[x][y+1] & Cell.VISITED == 0:
				children.append([x, y+1])

		return children

	def remove_common_wall(self, current_cell, random_child, unit_v):
		parent_x = current_cell[0]
		parent_y = current_cell[1]
		child_x = random_child[0]
		child_y = random_child[1]

		if unit_v[0] == 1: # right
			self.maze[parent_x][parent_y] &= ~Cell.RIGHTWALL
			self.maze[child_x][child_y] &= ~Cell.LEFTWALL
		if unit_v[0] == -1: #left
			self.maze[parent_x][parent_y] &= ~Cell.LEFTWALL
			self.maze[child_x][child_y] &= ~Cell.RIGHTWALL
		if unit_v[1] == 1: #up
			self.maze[parent_x][parent_y] &= ~Cell.UPWALL
			self.maze[child_x][child_y] &= ~Cell.DOWNWALL
		if unit_v[1] == -1: #down
			self.maze[parent_x][parent_y] &= ~Cell.DOWNWALL
			self.maze[child_x][child_y] &= ~Cell.UPWALL