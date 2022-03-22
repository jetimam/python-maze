from BFS_Search import BFS
from AS_Search import AS

class Agent:
	def __init__(self, position, maze):
		self.position = position
		self.maze = maze

	def set_position(self, destination): # for movement
		self.position = destination

	def goal_test(self, goal_position):
		return self.position == goal_position

	def search_BFS(self, goal_position):
		return BFS.search(self.maze, self.position, goal_position)

	def search_BFS_debug(self, screen, goal_position, CELL_SIZE):
		return BFS.search_debug(screen, self.maze, self.position, goal_position, CELL_SIZE)

	def search_AS(self, goal_position, heuristic):
		return AS.search(self.maze, self.position, goal_position, heuristic)
	
	def search_AS_debug(self, screen, goal_position, heuristic, CELL_SIZE):
		return AS.search_debug(screen, self.maze, self.position, goal_position, heuristic, CELL_SIZE)