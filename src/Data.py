from Agent import Agent
from Maze import Maze
from Position import Position
import csv
import time

user_pos = Position(0, 0)

with open('/Users/jetimam/Documents/BSP04/python-maze/data/BFS_data.csv', 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['Maze Size', 'Execution Time', 'Shortest Path Length'])
	cap = 5
	while(cap <= 205):
		for i in range(30):
			maze = Maze(cap)
			maze.initialize()
			agent = Agent(Position(cap-1, cap-1), maze)
			print('running bfs', cap)
			startTime = time.time()
			path = agent.BFS(user_pos)
			executionTime = (time.time() - startTime)
			rows = [cap, executionTime, len(path)]
			print('dumping data')
			csvwriter.writerow(rows)
		cap += 20