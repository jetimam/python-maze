from queue import Queue
import Util

def search(maze, start_position, goal_position, debug, screen):
	queue = Queue(0)
	backtracking_table = {}
	visited = {}
	visited[start_position] = True
	queue.put(start_position)
	# n = 0
	while not queue.empty():
		current_cell = queue.get()
		if debug:
			Util.draw_rect_debug(screen, Util.PURPLE, current_cell)
		# n += 1
		if current_cell == goal_position:
			break
		else:
			children = maze.generate_children_agent_traversal(current_cell, visited)
			for child in children:
				visited[child] = True
				queue.put(child)
				backtracking_table[child] = current_cell

	path = back_track(current_cell, backtracking_table, start_position, debug, screen)
	return path

def back_track(current_cell, backtracking_table, start_position, debug, screen):
	path = []

	path.append(current_cell)
	while current_cell != start_position:
		if debug:
			Util.draw_rect_debug(screen, Util.GREEN, current_cell)
		path.append(backtracking_table[current_cell])
		current_cell = backtracking_table[current_cell]

	path.reverse()
	return path