class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self) -> str:
		return '(' + str(self.x) + ', ' + str(self.y) + '):'

	def subtract(self, second_point):
		return Position(second_point.x - self.x, second_point.y - self.y)