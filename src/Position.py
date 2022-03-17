class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self) -> str:
		return '(' + str(self.x) + ', ' + str(self.y) + '):'

	def __hash__(self) -> int:
		return hash((self.x, self.y))

	def __eq__(self, __o: object) -> bool:
		return __o and self.x == __o.x and self.y == __o.y

	def __lt__ (self, other):
		if self.x == other.x:
			return self.y < other.y
		return self.x < other.x

	def subtract(self, parent):
		return Position(self.x - parent.x, self.y - parent.y)