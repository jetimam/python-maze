from queue import Queue
import pygame

class BFS:
	def search(maze, start_position, goal_position):
		queue = Queue(0)
		backtracking_table = {}
		visited = {}
		visited[start_position] = True
		queue.put(start_position)
		# n = 0
		while not queue.empty():
			current_cell = queue.get()
			# n += 1
			if current_cell == goal_position:
				break
			else:
				children = maze.generate_children_agent_traversal(current_cell, visited)
				for child in children:
					visited[child] = True
					queue.put(child)
					backtracking_table[child] = current_cell

		path = BFS.back_track(current_cell, backtracking_table, start_position)
		return path

	def search_debug(screen, maze, start_position, goal_position, CELL_SIZE):
		queue = Queue(0)
		backtracking_table = {}
		visited = {}
		visited[start_position] = True
		queue.put(start_position)
		# n = 0
		while not queue.empty():
			current_cell = queue.get()
			BFS.draw_rect(screen, (255, 0, 255), current_cell, CELL_SIZE)
			# n += 1
			if current_cell == goal_position:
				break
			else:
				children = maze.generate_children_agent_traversal(current_cell, visited)
				for child in children:
					visited[child] = True
					queue.put(child)
					backtracking_table[child] = current_cell

		path = BFS.back_track_debug(screen, current_cell, backtracking_table, start_position, CELL_SIZE)
		return path

	def back_track(current_cell, backtracking_table, start_position):
		path = []

		path.append(current_cell)
		while current_cell != start_position:
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		return path

	def back_track_debug(screen, current_cell, backtracking_table, start_position, CELL_SIZE):
		path = []

		path.append(current_cell)
		while current_cell != start_position:
			BFS.draw_rect(screen, (0, 255, 0), current_cell, CELL_SIZE)
			path.append(backtracking_table[current_cell])
			current_cell = backtracking_table[current_cell]

		path.reverse()
		return path

	def draw_rect(screen, color, position, CELL_SIZE):
		x = BFS.translate_coordinates(position.x, CELL_SIZE)
		y = BFS.translate_coordinates(position.y, CELL_SIZE)
		pygame.draw.rect(screen, color, pygame.Rect(x, y, CELL_SIZE/2, CELL_SIZE/2))
		pygame.display.update()
		print('drew rect')
		pygame.time.wait(500)

	def translate_coordinates(position, CELL_SIZE):
		return (position+0.5) * (CELL_SIZE)