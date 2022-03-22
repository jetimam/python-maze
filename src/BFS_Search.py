from queue import Queue

class BFS:
	def search(maze, start_position, goal_position):
		queue = Queue(0)
		backtracking_table = {}
		visited = {}
		visited[start_position] = True
		queue.put(start_position)
		while not queue.empty():
			current_cell = queue.get()
			if current_cell == goal_position:
				break
			else:
				children = maze.generate_children_agent_traversal(current_cell, visited)
				for child in children:
					visited[child] = True
					queue.put(child)
					backtracking_table[child] = current_cell
					
		return BFS.back_track(current_cell, backtracking_table, start_position)

	def back_track(current_cell, backtracking_table, start_position):
		path = []

		path.append(current_cell)
		while current_cell != start_position:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		return path