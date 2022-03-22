from Cell import Cell
from random import randint
from Position import Position

class Maze:
	def __init__(self, height):
		self.height = height
		self.maze = []
	
	def initialize(self):
		initial = Cell.UPWALL | Cell.RIGHTWALL | Cell.DOWNWALL | Cell.LEFTWALL # 0 1111
		self.maze = [[initial for _ in range(self.height)] for _ in range(self.height)]
		return self.DFS()

	def DFS(self):
		stack = []
		counter = 0
		initial_position = Position(0, 0)
		stack.append(initial_position)
		unit_v = Position(0, 0)
		while len(stack) > 0:
			current_cell_position = stack.pop()
			self.maze[current_cell_position.x][current_cell_position.y] |= Cell.VISITED
			children = self.generate_children_maze_build(current_cell_position)
			if len(children) > 0:
				if len(children) > 1:
					stack.append(current_cell_position) # so that the other children can be explored when we eventually backtrack
				random_child_position = children[randint(0, len(children)-1)]
				unit_v = random_child_position.subtract(current_cell_position) # indicates the direction from current->child
				self.remove_common_wall(current_cell_position, random_child_position, unit_v)
				stack.append(random_child_position)
			else:
				counter += 1
				if counter == 3:
					self.remove_deadend(unit_v, current_cell_position)
					counter = 0

		return self.maze

	def generate_children_maze_build(self, current_cell_position):
		children = []
		x = current_cell_position.x
		y = current_cell_position.y

		if x > 0: #left border
			if self.maze[x - 1][y] & Cell.VISITED == 0:
				children.append(Position(x - 1, y))
		if y > 0: #up border
			if self.maze[x][y - 1] & Cell.VISITED == 0:
				children.append(Position(x, y - 1))
		if x <= self.height - 2: #right border
			if self.maze[x + 1][y] & Cell.VISITED == 0:
				children.append(Position(x + 1, y))
		if y <= self.height - 2: #down border
			if self.maze[x][y + 1] & Cell.VISITED == 0:
				children.append(Position(x, y + 1))

		return children

	def remove_common_wall(self, current_cell_position, random_child_position, unit_v):
		if unit_v.x == 1: # right
			self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.RIGHTWALL # 1111 & 1101 = 1101
			self.maze[random_child_position.x][random_child_position.y] &= ~Cell.LEFTWALL
		elif unit_v.x == -1: #left
			self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.LEFTWALL
			self.maze[random_child_position.x][random_child_position.y] &= ~Cell.RIGHTWALL
		elif unit_v.y == 1: #down
			self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.DOWNWALL
			self.maze[random_child_position.x][random_child_position.y] &= ~Cell.UPWALL
		elif unit_v.y == -1: #up
			self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.UPWALL
			self.maze[random_child_position.x][random_child_position.y] &= ~Cell.DOWNWALL

	def remove_deadend(self, unit_v, current_cell_position):
		if unit_v.x == 1: # right
			if current_cell_position.x < self.height-2:
				self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.RIGHTWALL # 1111 & 1101 = 1101
				self.maze[current_cell_position.x + 1][current_cell_position.y] &= ~Cell.LEFTWALL
		elif unit_v.x == -1: # left
			if current_cell_position.x > 0:
				self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.LEFTWALL
				self.maze[current_cell_position.x - 1][current_cell_position.y] &= ~Cell.RIGHTWALL
		elif unit_v.y == 1: # down
			if current_cell_position.y < self.height-2:
				self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.DOWNWALL
				self.maze[current_cell_position.x][current_cell_position.y + 1] &= ~Cell.UPWALL
		elif unit_v.y == -1: # up
			if current_cell_position.y > 0:
				self.maze[current_cell_position.x][current_cell_position.y] &= ~Cell.UPWALL
				self.maze[current_cell_position.x][current_cell_position.y - 1] &= ~Cell.DOWNWALL

	def generate_children_agent_traversal(self, current_cell_position, visited):
		children = []
		x = current_cell_position.x
		y = current_cell_position.y

		if x > 0: #left border
			if Position(x-1,y) not in visited and self.maze[x-1][y] & Cell.RIGHTWALL == 0: # this "key in dict" operation's time complexity is O(1)
				children.append(Position(x-1, y))
		if y > 0: #up border
			if Position(x,y-1) not in visited and self.maze[x][y-1] & Cell.DOWNWALL == 0:
				children.append(Position(x, y-1))
		if x <= self.height-2: #right border
			if Position(x+1,y) not in visited and self.maze[x+1][y] & Cell.LEFTWALL == 0:
				children.append(Position(x+1, y))
		if y <= self.height-2: #down border
			if Position(x,y+1) not in visited and self.maze[x][y+1] & Cell.UPWALL == 0:
				children.append(Position(x, y+1))

		return children

	def get_value(self, i, j):
		return self.maze[i][j]