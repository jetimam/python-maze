from queue import PriorityQueue
import Util

def search(maze, start_position, goal_position, heuristic, debug, screen):
	priority_queue = PriorityQueue()
	backtracking_table = {}
	visited = {}
	visited[start_position] = True
	f_score = heuristic(start_position.x, start_position.y, goal_position.x, goal_position.y)
	priority_queue.put((f_score, (0, start_position)))
	# n = 0
	while priority_queue.not_empty:
		current_cell = priority_queue.get()
		if debug:
			Util.draw_rect_debug(screen, Util.PURPLE, current_cell[1][1])
		# n += 1
		if current_cell[1][1] == goal_position:
			break
		else:
			children_position = maze.generate_children_agent_traversal(current_cell[1][1], visited)
			for child_position in children_position:
				g_score = current_cell[1][0] + 1
				h_score = Util.heuristic_weight * heuristic(child_position.x, child_position.y, goal_position.x, goal_position.y)
				f_score = g_score + h_score
				visited[child_position] = True
				backtracking_table[child_position] = current_cell[1][1]
				priority_queue.put((f_score, (g_score, child_position)))
	path = back_track(current_cell[1][1], backtracking_table, start_position, debug, screen)
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