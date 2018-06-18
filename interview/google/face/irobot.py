"""
已知扫地机器人有move(), turn_left(k), turn_right(k), clean()方法，机器人能面向东南西北四个方向，
move是按当前方向移动一格，如果不能移动返回false; turn_left(k), turn_right(k)是旋转k*90度; 
房间里可能有障碍物，机器人并不知道房间的布局，设计算法让扫地机器人清扫房间（走完房间每一格）。
"""

#move(), turn_left(k), turn_right(k), clean()
def clean(t):
	i, j = 0, 0
	visited = set()
	dirc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	# Assumption: default direction
	dr = 0
	def l():
		turn_left()
		dr += 1
		dr %= 4
	def r():
		turn_right()
		dr -= 1
		dr %= 4
	def move_front():
		if move():
			i += dirc[dr][0]
			j += dirc[dr][1]
			return True
		return False
	def move_back():
		l()
		l()
		move_front()
	def search():
		if (i, j) in visited:
			return
		visited.add((i, j))
		clean()
		# left		
		l()
		if move_front():
			search()
			move_back()
		r()
		
		# front		
		if move_front():
		search()
		move_back()
		
		# right
		r()
		if move_front():
			search()
			move_back()
		l()