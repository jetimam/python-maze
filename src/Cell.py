from enum import IntFlag

class Cell(IntFlag):
		UPWALL = 1
		RIGHTWALL = 2
		DOWNWALL = 4
		LEFTWALL = 8
		VISITED = 16