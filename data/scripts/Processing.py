import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dir_path="/Users/jetimam/Documents/BSP04/python-maze/data/"

df = pd.read_csv(dir_path + "FINAL/AS_vs_BFS_FINAL.csv")
df_center = df.loc[(df['Starting Position'] == 'center')]
df = df.loc[(df['Starting Position'] == 'corner')]

# fig = plt.figure()
# fig, ax = plt.subplots()
# ax.plot(df[['Maze Size']], df[['BFS Shortest Path Length']], label='BFS')
# ax.plot(df[['Maze Size']], df[['AS Euclidean Shortest Path Length']], label='AS Euclidean')
# ax.plot(df[['Maze Size']], df[['AS Manhattan Shortest Path Length']], label='AS Manhattan')
# ax.set_xlabel('Maze Size')
# ax.set_ylabel('Shortest Path Length')
# ax.set_title("Maze Size to Shortest Path Length")
# ax.legend()
# plt.show()


# sub_df = df.loc[(df['Maze Size'] == 300) & (df['Starting Position'] == 'corner') & (df['Heuristic Weight'] == 1)] # ==> all rows that are: center and h(x) = 1
# sub_df = sub_df[['Wall Rate', 'BFS Shortest Path Length', 'AS Euclidean Shortest Path Length', 'AS Manhattan Shortest Path Length']]
# sub_df = sub_df.groupby(['Wall Rate']).mean()
# print(sub_df)
# sub_df.plot()
# plt.show()


# sub_df = df.loc[(df['Maze Size'] == 300) & (df['Starting Position'] == 'center')]
# sub_df = df[['Heuristic Weight', 'BFS Shortest Path Length', 'AS Euclidean Shortest Path Length', 'AS Manhattan Shortest Path Length']]
# sub_df = sub_df.groupby(['Heuristic Weight']).mean()
# sub_df.plot()
# plt.show()

# Shortest Path Length / Maze Size
fig, ax = plt.subplots()

as_man_shortest_path_mean = df[['Maze Size', 'AS Manhattan Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_shortest_path_std = df[['Maze Size', 'AS Manhattan Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_shortest_path_mean, label='AS Manhattan Shortest Path Length')
confidence_interval = 1.96 * as_man_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_shortest_path_mean - confidence_interval), (as_man_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_shortest_path_mean = df[['Maze Size', 'AS Euclidean Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_shortest_path_std = df[['Maze Size', 'AS Euclidean Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_shortest_path_mean, label='AS Euclidean Shortest Path Length')
confidence_interval = 1.96 * as_euc_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_shortest_path_mean - confidence_interval), (as_euc_shortest_path_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

bfs_shortest_path_mean = df[['Maze Size', 'BFS Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_shortest_path_std = df[['Maze Size', 'BFS Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_shortest_path_mean, label='BFS Shortest Path Length')
confidence_interval = 1.96 * bfs_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_shortest_path_mean - confidence_interval), (bfs_shortest_path_mean + confidence_interval), alpha=.1, color='green')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Maze Size', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Shortest Path Length', fontdict=None, labelpad=None, loc=None)
plt.show()

# Expanded Nodes / Maze Size
fig, ax = plt.subplots()

as_man_expanded_nodes_mean = df[['Maze Size', 'AS Manhattan Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_expanded_nodes_std = df[['Maze Size', 'AS Manhattan Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_expanded_nodes_mean, label='AS Manhattan Expanded Nodes')
confidence_interval = 1.96 * as_man_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_expanded_nodes_mean - confidence_interval), (as_man_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_expanded_nodes_mean = df[['Maze Size', 'AS Euclidean Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_expanded_nodes_std = df[['Maze Size', 'AS Euclidean Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_expanded_nodes_mean, label='AS Euclidean Expanded Nodes')
confidence_interval = 1.96 * as_euc_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_expanded_nodes_mean - confidence_interval), (as_euc_expanded_nodes_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

bfs_expanded_nodes_mean = df[['Maze Size', 'BFS Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_expanded_nodes_std = df[['Maze Size', 'BFS Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_expanded_nodes_mean, label='BFS Expanded Nodes')
confidence_interval = 1.96 * bfs_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_expanded_nodes_mean - confidence_interval), (bfs_expanded_nodes_mean + confidence_interval), alpha=.1, color='green')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Maze Size', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Expanded Nodes', fontdict=None, labelpad=None, loc=None)
plt.show()

# Shortest Path / Heuristic Weight
fig, ax = plt.subplots()

as_man_shortest_path_mean = df[['Heuristic Weight', 'AS Manhattan Shortest Path Length']].groupby(['Heuristic Weight']).mean().to_numpy().flatten()
as_man_shortest_path_std = df[['Heuristic Weight', 'AS Manhattan Shortest Path Length']].groupby(['Heuristic Weight']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_man_shortest_path_mean, label='AS Manhattan Shortest Path Length')
confidence_interval = 1.96 * as_man_shortest_path_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_man_shortest_path_mean - confidence_interval), (as_man_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_shortest_path_mean = df[['Heuristic Weight', 'AS Euclidean Shortest Path Length']].groupby(['Heuristic Weight']).mean().to_numpy().flatten()
as_euc_shortest_path_std = df[['Heuristic Weight', 'AS Euclidean Shortest Path Length']].groupby(['Heuristic Weight']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_euc_shortest_path_mean, label='AS Euclidean Shortest Path Length')
confidence_interval = 1.96 * as_euc_shortest_path_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_euc_shortest_path_mean - confidence_interval), (as_euc_shortest_path_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Heuristic Weight', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Shortest Path Length', fontdict=None, labelpad=None, loc=None)
plt.show()

# Expanded Nodes / Heuristic Weight
fig, ax = plt.subplots()

as_man_expanded_nodes_mean = df[['Heuristic Weight', 'AS Manhattan Expanded Nodes']].groupby(['Heuristic Weight']).mean().to_numpy().flatten()
as_man_expanded_nodes_std = df[['Heuristic Weight', 'AS Manhattan Expanded Nodes']].groupby(['Heuristic Weight']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_man_expanded_nodes_mean, label='AS Manhattan Expanded Nodes')
confidence_interval = 1.96 * as_man_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_man_expanded_nodes_mean - confidence_interval), (as_man_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_expanded_nodes_mean = df[['Heuristic Weight', 'AS Euclidean Expanded Nodes']].groupby(['Heuristic Weight']).mean().to_numpy().flatten()
as_euc_expanded_nodes_std = df[['Heuristic Weight', 'AS Euclidean Expanded Nodes']].groupby(['Heuristic Weight']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_euc_expanded_nodes_mean, label='AS Euclidean Expanded Nodes')
confidence_interval = 1.96 * as_euc_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_euc_expanded_nodes_mean - confidence_interval), (as_euc_expanded_nodes_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Heuristic Weight', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Expanded Nodes', fontdict=None, labelpad=None, loc=None)
plt.show()

# Shortest Path / Wall Rate
fig, ax = plt.subplots()

as_man_shortest_path_mean = df[['Wall Rate', 'AS Manhattan Shortest Path Length']].groupby(['Wall Rate']).mean().to_numpy().flatten()
as_man_shortest_path_std = df[['Wall Rate', 'AS Manhattan Shortest Path Length']].groupby(['Wall Rate']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_man_shortest_path_mean, label='AS Manhattan Shortest Path Length')
confidence_interval = 1.96 * as_man_shortest_path_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_man_shortest_path_mean - confidence_interval), (as_man_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_shortest_path_mean = df[['Wall Rate', 'AS Euclidean Shortest Path Length']].groupby(['Wall Rate']).mean().to_numpy().flatten()
as_euc_shortest_path_std = df[['Wall Rate', 'AS Euclidean Shortest Path Length']].groupby(['Wall Rate']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_euc_shortest_path_mean, label='AS Euclidean Shortest Path Length')
confidence_interval = 1.96 * as_euc_shortest_path_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_euc_shortest_path_mean - confidence_interval), (as_euc_shortest_path_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

bfs_shortest_path_length_mean = df[['Wall Rate', 'BFS Shortest Path Length']].groupby(['Wall Rate']).mean().to_numpy().flatten()
bfs_shortest_path_length_std = df[['Wall Rate', 'BFS Shortest Path Length']].groupby(['Wall Rate']).std().to_numpy().flatten()
ax.plot(range(1, 6), bfs_shortest_path_length_mean, label='BFS Shortest Path Length')
confidence_interval = 1.96 * bfs_shortest_path_length_std / np.sqrt(50)
ax.fill_between(range(1, 6), (bfs_shortest_path_length_mean - confidence_interval), (bfs_shortest_path_length_mean + confidence_interval), alpha=.1, color='green')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Wall Rate', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Shortest Path Length', fontdict=None, labelpad=None, loc=None)
plt.show()

# Expanded Nodes / Wall Rate
fig, ax = plt.subplots()

as_man_expanded_nodes_mean = df[['Wall Rate', 'AS Manhattan Expanded Nodes']].groupby(['Wall Rate']).mean().to_numpy().flatten()
as_man_expanded_nodes_std = df[['Wall Rate', 'AS Manhattan Expanded Nodes']].groupby(['Wall Rate']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_man_expanded_nodes_mean, label='AS Manhattan Expanded Nodes')
confidence_interval = 1.96 * as_man_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_man_expanded_nodes_mean - confidence_interval), (as_man_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_expanded_nodes_mean = df[['Wall Rate', 'AS Euclidean Expanded Nodes']].groupby(['Wall Rate']).mean().to_numpy().flatten()
as_euc_expanded_nodes_std = df[['Wall Rate', 'AS Euclidean Expanded Nodes']].groupby(['Wall Rate']).std().to_numpy().flatten()
ax.plot(range(1, 6), as_euc_expanded_nodes_mean, label='AS Euclidean Expanded Nodes')
confidence_interval = 1.96 * as_euc_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(1, 6), (as_euc_expanded_nodes_mean - confidence_interval), (as_euc_expanded_nodes_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

bfs_expanded_nodes_mean = df[['Wall Rate', 'BFS Expanded Nodes']].groupby(['Wall Rate']).mean().to_numpy().flatten()
bfs_expanded_nodes_std = df[['Wall Rate', 'BFS Expanded Nodes']].groupby(['Wall Rate']).std().to_numpy().flatten()
ax.plot(range(1, 6), bfs_expanded_nodes_mean, label='BFS Expanded Nodes')
confidence_interval = 1.96 * bfs_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(1, 6), (bfs_expanded_nodes_mean - confidence_interval), (bfs_expanded_nodes_mean + confidence_interval), alpha=.1, color='green')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Wall Rate', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Expanded Nodes', fontdict=None, labelpad=None, loc=None)
plt.show()

# Execution Time / Maze Size
fig, ax = plt.subplots()

as_man_execution_time_mean = df[['Maze Size', 'AS Manhattan Execution Time']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_execution_time_std = df[['Maze Size', 'AS Manhattan Execution Time']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_execution_time_mean, label='AS Manhattan Execution Time')
confidence_interval = 1.96 * as_man_execution_time_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_execution_time_mean - confidence_interval), (as_man_execution_time_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_execution_time_mean = df[['Maze Size', 'AS Euclidean Execution Time']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_execution_time_std = df[['Maze Size', 'AS Euclidean Execution Time']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_execution_time_mean, label='AS Euclidean Execution Time')
confidence_interval = 1.96 * as_euc_execution_time_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_execution_time_mean - confidence_interval), (as_euc_execution_time_mean + confidence_interval), alpha=.1, color='red')
plt.legend(loc='best', fontsize='small')

bfs_execution_time_mean = df[['Maze Size', 'BFS Execution Time']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_execution_time_std = df[['Maze Size', 'BFS Execution Time']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_execution_time_mean, label='BFS Execution Time')
confidence_interval = 1.96 * bfs_execution_time_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_execution_time_mean - confidence_interval), (bfs_execution_time_mean + confidence_interval), alpha=.1, color='green')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Maze Size', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Execution Time', fontdict=None, labelpad=None, loc=None)
plt.show()

# Shortest Path Length / Maze Size (CORNER VS CENTER)
fig, ax = plt.subplots()

as_man_corner_shortest_path_mean = df[['Maze Size', 'AS Manhattan Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_corner_shortest_path_std = df[['Maze Size', 'AS Manhattan Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_corner_shortest_path_mean, label='AS Manhattan Shortest Path Length (Corner)')
confidence_interval = 1.96 * as_man_corner_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_corner_shortest_path_mean - confidence_interval), (as_man_corner_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_man_center_shortest_path_mean = df_center[['Maze Size', 'AS Manhattan Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_center_shortest_path_std = df_center[['Maze Size', 'AS Manhattan Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_center_shortest_path_mean, label='AS Manhattan Shortest Path Length (Center)')
confidence_interval = 1.96 * as_man_center_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_center_shortest_path_mean - confidence_interval), (as_man_center_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')


as_euc_corner_shortest_path_mean = df[['Maze Size', 'AS Euclidean Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_corner_shortest_path_std = df[['Maze Size', 'AS Euclidean Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_corner_shortest_path_mean, label='AS Euclidean Shortest Path Length (Corner)')
confidence_interval = 1.96 * as_euc_corner_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_corner_shortest_path_mean - confidence_interval), (as_euc_corner_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_center_shortest_path_mean = df_center[['Maze Size', 'AS Euclidean Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_center_shortest_path_std = df_center[['Maze Size', 'AS Euclidean Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_center_shortest_path_mean, label='AS Euclidean Shortest Path Length (Center)')
confidence_interval = 1.96 * as_euc_center_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_center_shortest_path_mean - confidence_interval), (as_euc_center_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')


bfs_corner_shortest_path_mean = df[['Maze Size', 'BFS Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_corner_shortest_path_std = df[['Maze Size', 'BFS Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_corner_shortest_path_mean, label='BFS Shortest Path Length (Corner)')
confidence_interval = 1.96 * bfs_corner_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_corner_shortest_path_mean - confidence_interval), (bfs_corner_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

bfs_center_shortest_path_mean = df_center[['Maze Size', 'BFS Shortest Path Length']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_center_shortest_path_std = df_center[['Maze Size', 'BFS Shortest Path Length']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_center_shortest_path_mean, label='BFS Shortest Path Length (Center)')
confidence_interval = 1.96 * bfs_center_shortest_path_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_center_shortest_path_mean - confidence_interval), (bfs_center_shortest_path_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Maze Size', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Shortest Path Length', fontdict=None, labelpad=None, loc=None)
plt.show()

# Expanded Nodes / Maze Size (CORNER VS CENTER)
fig, ax = plt.subplots()

as_man_corner_expanded_nodes_mean = df[['Maze Size', 'AS Manhattan Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_corner_expanded_nodes_std = df[['Maze Size', 'AS Manhattan Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_corner_expanded_nodes_mean, label='AS Manhattan Expanded Nodes (Corner)')
confidence_interval = 1.96 * as_man_corner_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_corner_expanded_nodes_mean - confidence_interval), (as_man_corner_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_man_center_expanded_nodes_mean = df_center[['Maze Size', 'AS Manhattan Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_man_center_expanded_nodes_std = df_center[['Maze Size', 'AS Manhattan Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_man_center_expanded_nodes_mean, label='AS Manhattan Expanded Nodes (Center)')
confidence_interval = 1.96 * as_man_center_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_man_center_expanded_nodes_mean - confidence_interval), (as_man_center_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')


as_euc_corner_expanded_nodes_mean = df[['Maze Size', 'AS Euclidean Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_corner_expanded_nodes_std = df[['Maze Size', 'AS Euclidean Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_corner_expanded_nodes_mean, label='AS Euclidean Expanded Nodes (Corner)')
confidence_interval = 1.96 * as_euc_corner_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_corner_expanded_nodes_mean - confidence_interval), (as_euc_corner_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

as_euc_center_expanded_nodes_mean = df_center[['Maze Size', 'AS Euclidean Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
as_euc_center_expanded_nodes_std = df_center[['Maze Size', 'AS Euclidean Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), as_euc_center_expanded_nodes_mean, label='AS Euclidean Expanded Nodes (Center)')
confidence_interval = 1.96 * as_euc_center_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (as_euc_center_expanded_nodes_mean - confidence_interval), (as_euc_center_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')


bfs_corner_expanded_nodes_mean = df[['Maze Size', 'BFS Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_corner_expanded_nodes_std = df[['Maze Size', 'BFS Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_corner_expanded_nodes_mean, label='BFS Expanded Nodes (Corner)')
confidence_interval = 1.96 * bfs_corner_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_corner_expanded_nodes_mean - confidence_interval), (bfs_corner_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

bfs_center_expanded_nodes_mean = df_center[['Maze Size', 'BFS Expanded Nodes']].groupby(['Maze Size']).mean().to_numpy().flatten()
bfs_center_expanded_nodes_std = df_center[['Maze Size', 'BFS Expanded Nodes']].groupby(['Maze Size']).std().to_numpy().flatten()
ax.plot(range(5, 301, 5), bfs_center_expanded_nodes_mean, label='BFS Expanded Nodes (Center)')
confidence_interval = 1.96 * bfs_center_expanded_nodes_std / np.sqrt(50)
ax.fill_between(range(5, 301, 5), (bfs_center_expanded_nodes_mean - confidence_interval), (bfs_center_expanded_nodes_mean + confidence_interval), alpha=.1, color='blue')
plt.legend(loc='best', fontsize='small')

plt.xlabel('Maze Size', fontdict=None, labelpad=None, loc=None)
plt.ylabel('Expanded Nodes', fontdict=None, labelpad=None, loc=None)
plt.show()