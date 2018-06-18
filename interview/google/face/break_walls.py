#!/bin/bash
class break_walls:
	
	def __init__(self, grid, start_x, start_y):
		self.grid = grid
		self.current_x = start_x
		self.current_y = start_y
		self.direction = 0
		
	def check_success():
		if current_x < 0 || current_x >= len(grid[0]):
			return True
		if current_y < 0 || current_y >= len(grid):
			return True
		return False
		
	def turn_90(self):
		self.direction += 1
		self.direction %= 4
		print "turn"

	def move(self):
		next_x, next_y = self.current_x, self.current_y
		if self.direction == 0:
			next_x += 1
		else if self.direciton == 1:
			next_y += 1
		else if self.direction == 2:
			next_x -= 1
		else:
			next_y -= 1
		if self.grid[next_x][next_y] == 'w'
		print move, current_x, current_y
	
	def moveBack(self):
		self.turn_90()
		self.turn_90()
		self.move()
	
	def next_step(self):
#		move 3 direction
		self.move()
		if self.check_success():
			return True
		
		
	
