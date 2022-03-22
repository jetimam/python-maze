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

	def search_AS(self, goal_position, heuristic):
		return AS.search(self.maze, self.position, goal_position, heuristic)