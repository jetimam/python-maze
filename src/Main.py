from Maze import Maze
import pygame

# # setup window
# FPS = 30
# S_HEIGHT = 600
M_HEIGHT = 5
# CELL_SIZE = S_HEIGHT // M_HEIGHT

# maze config
maze = Maze(M_HEIGHT, M_HEIGHT)
maze.initialize()

# # colors
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 225)
# YELLOW = (255, 255, 0)

# # pygame init
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((S_HEIGHT, S_HEIGHT))
# pygame.display.set_caption("Python Maze")
# clock = pygame.time.Clock()

# def render_grid():
# 	for i in range(0, S_HEIGHT, CELL_SIZE):
# 		for j in range(0, S_HEIGHT, CELL_SIZE):
# 			rect = pygame.Rect(i, j, CELL_SIZE, CELL_SIZE)
# 			pygame.draw.rect(screen, WHITE, rect, 1)
# 			pygame.display.update()

# # render maze
# render_grid()

# # game loop
# while True:
# 	clock.tick(FPS)
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			break