import sys
sys.path.append("/Users/jetimam/Documents/BSP04/python-maze/src")
from Agent import Agent
from Maze import Maze
from Position import Position
from Cell import Cell
import csv
import time
import math

def BFS_generation(cap, user_pos):
	n = 5
	with open("/Users/jetimam/Documents/BSP04/python-maze/data/in_progress/BFS.csv", 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['Maze Size', 'Execution Time', 'Shortest Path Length', 'Expanded Nodes'])
		while n <= cap:
			for i in range(30):
				maze = Maze(n)
				maze.initialize()
				agent = Agent(Position(n-1, n-1), maze)
				print('running bfs', n)
				print('turn', i)
				startTime = time.time()
				path = agent.search_BFS(user_pos)
				executionTime = (time.time() - startTime)
				rows = [n, executionTime, len(path[0]), path[1]]
				print('dumping data')
				csvwriter.writerow(rows)
			n += 5

def AS_generation(cap, user_pos, heuristic, heuristic_str):
	n = 5
	with open("/Users/jetimam/Documents/BSP04/python-maze/data/in_progress/AS_"+ heuristic_str + ".csv", 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['Maze Size', 'Execution Time', 'Shortest Path Length', 'Expanded Nodes'])
		while n <= cap:
			for i in range(30):
				maze = Maze(n)
				maze.initialize()
				agent = Agent(Position(n-1, n-1), maze)
				print('running', heuristic_str, n)
				print('turn', i)
				startTime = time.time()
				path = agent.search_AS(user_pos, heuristic)
				executionTime = (time.time() - startTime)
				rows = [n, executionTime, len(path[0]), path[1]]
				print('dumping data')
				csvwriter.writerow(rows)
			n += 5

def AS_BFS_joint_generation(cap, user_pos, heuristic, heuristic_str, mul):
	mul += 1
	n = 5
	with open("/Users/jetimam/Documents/BSP04/python-maze/data/in_progress/joint/AS_"+ heuristic_str + "_vs_BFS2.csv", 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['Maze Size', 'Wall Amount', 'Starting Position', 'Heuristic Weight', 'BFS Execution Time', 'AS Execution Time', 'BFS Shortest Path Length', 'AS Shortest Path Length', 'BFS Expanded Nodes', 'AS Expanded Nodes'])
		while n <= cap:
			for mul_temp in range(1, mul):
				for i in range(50):
					maze = Maze(n)
					maze.initialize()
					wall_amount = count_walls(maze, n)

					agent = Agent(Position(n-1, n-1), maze)
					print('turn', i, '| size', n, "corner |", mul_temp)
					print('running bfs')
					start_time = time.time()
					bfs_data = agent.search_BFS(user_pos)
					bfs_execution_time = (time.time() - start_time)
					print('running', heuristic_str)
					start_time = time.time()
					as_data = agent.search_AS(user_pos, heuristic, mul)
					as_execution_time = (time.time() - start_time)
					rows = [n, wall_amount, "corner", mul_temp, bfs_execution_time, as_execution_time, len(bfs_data[0]), len(as_data[0]), bfs_data[1], as_data[1]]
					print('dumping data, A*:', as_execution_time, "BFS:", bfs_execution_time)
					csvwriter.writerow(rows)

					agent = Agent(Position((n//2), (n//2)), maze)
					print('turn', i, '| size', n, "center |", mul_temp)
					print('running bfs')
					start_time = time.time()
					bfs_data = agent.search_BFS(user_pos)
					bfs_execution_time = (time.time() - start_time)
					print('running', heuristic_str)
					start_time = time.time()
					as_data = agent.search_AS(user_pos, heuristic, mul)
					as_execution_time = (time.time() - start_time)
					rows = [n, wall_amount, "center", mul_temp, bfs_execution_time, as_execution_time, len(bfs_data[0]), len(as_data[0]), bfs_data[1], as_data[1]]
					print('dumping data, A*:', as_execution_time, "BFS:", bfs_execution_time)
					csvwriter.writerow(rows)
			n += 5

# def AS_wall_amount(cap, user_pos, heuristic, heuristic_str, mul):
# 	with open("/Users/jetimam/Documents/BSP04/python-maze/data/in_progress/AS_"+ heuristic_str + ".csv", 'w') as csvfile:
# 		csvwriter = csv.writer(csvfile)
# 		csvwriter.writerow(['Maze Size', 'Execution Time', 'Shortest Path Length', 'Expanded Nodes'])
# 		while n <= cap:
# 			for i in range(30):
# 				maze = Maze(n)
# 				maze.initialize()
# 				agent = Agent(Position(n-1, n-1), maze)
# 				print('running', heuristic_str, n)
# 				print('turn', i)
# 				startTime = time.time()
# 				path = agent.search_AS(user_pos, heuristic)
# 				executionTime = (time.time() - startTime)
# 				rows = [n, executionTime, len(path[0]), path[1]]
# 				print('dumping data')
# 				csvwriter.writerow(rows)
# 			n += 5

def count_walls(maze, n):
	walls = 0
	for i in range(n):
		for j in range(n):
			cell = maze.get_value(i, j)
			if cell & Cell.UPWALL == 1:
				walls += 1
			if cell & Cell.RIGHTWALL == 2:
				walls += 1
			if cell & Cell.DOWNWALL ==  4:
				walls += 1
			if cell & Cell.LEFTWALL == 8:
				walls += 1
	return walls/2

user_pos = Position(0, 0)
cap = 400
euclidean = lambda x,y,x_t,y_t: math.sqrt((x_t - x)**2 + (y_t - y)**2)
manhattan = lambda x, y, x_t, y_t: abs(x - x_t) + abs(y - y_t)

# BFS_generation(cap, user_pos)
# AS_generation(cap, user_pos, euclidean, "euclidean")
# AS_generation(cap, user_pos, manhattan, "manhattan")
AS_BFS_joint_generation(cap, user_pos, euclidean, "euclidean", 5)
AS_BFS_joint_generation(cap, user_pos, manhattan, "manhattan", 5)