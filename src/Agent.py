from queue import Queue

class Agent:
	def __init__(self, position, maze):
		self.position = position
		self.maze = maze

	def set_position(self, destination):
		self.position = destination

	def goal_test(self, goal_position):
		return self.position == goal_position

	def BFS(self, goal_position):
		queue = Queue(0)
		visited = []
		backtracking_table = {}
		queue.put(self.position)
		visited.append(self.position)
		while len(queue) > 0:
			current_cell = queue.get()
			visited.append(current_cell)

			if current_cell == goal_position:
				break
			else:
				children = self.generate_children(current_cell)

				for child in children:
					visited.append(child)
					queue.put(child)
					backtracking_table[child] = current_cell


	def generate_children(self, parent_cell, visited):
		children = []
		x = parent_cell[0]
		y = parent_cell[1]

		if x > 0: #left border
			if self.maze[x-1][y] not in visited:
				children.append([x-1, y])
		if y > 0: #up border
			if self.maze[x][y-1] not in visited:
				children.append([x, y-1])
		if x < self.width-2: #right border
			if self.maze[x+1][y] not in visited:
				children.append([x+1, y])
		if y < self.height-2: #down border
			if self.maze[x][y+1] not in visited:
				children.append([x, y+1])

		return children

	def back_track(self, current_cell, backtracking_table):
		path = []

		path.append(current_cell)
		while current_cell != self.spawn_point:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		return path