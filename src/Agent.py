from queue import Queue

class Agent:
	def __init__(self, position, maze):
		self.position = position
		self.maze = maze

	def set_position(self, destination): # for movement
		self.position = destination

	def goal_test(self, goal_position):
		return self.position == goal_position

	def BFS(self, goal_position):
		queue = Queue(0)
		visited = []
		backtracking_table = {}
		queue.put(self.position)
		visited.append(self.position)
		while not queue.empty():
			current_cell = queue.get()
			if current_cell == goal_position:
				break
			else:
				children = self.maze.generate_children_agent_traversal(current_cell, visited)
				for child in children:
					visited.append(child)
					queue.put(child)
					backtracking_table[child] = current_cell
					
		return self.back_track(current_cell, backtracking_table)

	def back_track(self, current_cell, backtracking_table):
		path = []

		path.append(current_cell)
		while current_cell != self.position:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		print(path)
		return path