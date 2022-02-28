class Clock:
	def __init__(self):
		self.clock = 1

	def timer(self, pygame_clock):
		if pygame_clock > self.clock:
			self.clock += 1
			return True
		return False