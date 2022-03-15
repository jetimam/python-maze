class AS:
	def search(maze, start_position, goal_position, heuristic):
		priority_queue = PriorityQueue()
		visited = []
		backtracking_table = {}
		f_score = heuristic(start_position.x, start_position.y, goal_position.x, goal_position.y)
		priority_queue.enqueue([f_score, 0, start_position])
		visited.append(start_position)
		while not priority_queue.is_empty():
			current_cell = priority_queue.dequeue()
			if current_cell[2] == goal_position:
				break
			else:
				children_position = maze.generate_children_agent_traversal(current_cell[2], visited)
				for child_position in children_position:
					unit_v = child_position.subtract(current_cell[2])
					g_score = current_cell[1] + (abs(unit_v.x+unit_v.y))
					h_score = heuristic(child_position.x, child_position.y, goal_position.x, goal_position.y)
					f_score = g_score + h_score
					visited.append(child_position)
					backtracking_table[child_position] = current_cell[2]
					priority_queue.enqueue([f_score, g_score, child_position])

		return AS.back_track(current_cell[2], backtracking_table, start_position)

	def back_track(current_cell, backtracking_table, start_position):
		path = []

		path.append(current_cell)
		while current_cell != start_position:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		return path

class PriorityQueue:
	def __init__(self):
		self.queue = []

	def __repr__(self) -> str:
		return ' '.join([str(i) for i in self.queue])

	def is_empty(self):
		return len(self.queue) == 0

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		x = self.queue[0][0]
		y = 0

		for i in range(len(self.queue)):
			if self.queue[i][0] < x:
				x = self.queue[i][0]
				y = i

		return self.queue.pop(y)