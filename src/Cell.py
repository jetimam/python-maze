from enum import IntFlag

class Cell(IntFlag):
		UPWALL = 1
		RIGHTWALL = 2
		DOWNWALL = 3
		LEFTWALL = 4
		VISITED = 5