from Cell import Cell

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
		stack.append([maze[1][1], (1, 1)])

		while(len(stack) > 0):
			current_cell = stack.pop()
			current_cell[0] | Cell.VISITED

			children = self.generate_children(current_cell[1], maze)

			print(children)
		return maze

	def generate_children(self, parent_coordinates, maze):
		children = []

		if parent_coordinates[0] > 0:
			children.append((parent_coordinates[0]-1, parent_coordinates[1]))
		if parent_coordinates[1] > 0:
			children.append((parent_coordinates[0], parent_coordinates[1]-1))
		if parent_coordinates[0] < self.height-1:
			children.append((parent_coordinates[0]+1, parent_coordinates[1]))
		if parent_coordinates[1] < self.width-1:
			children.append((parent_coordinates[0], parent_coordinates[1]+1))

		return children