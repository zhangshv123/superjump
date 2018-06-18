"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)

"""
"""
思路: 设计一个贪吃蛇游戏, 给定了长宽初始位置和食物位置, 并且每次给一个移动方向的指令. 可以用一个队列来保存当前蛇身体所占的位置, 
每次往队列中添加当前位置并且删除队首元素. 还需要判断的是当前位置是否到达边界和是否撞到了自身, 为了做这个判断可以用一个hash表来同样
存储映射一下蛇身体所占的位置, 这样做的好处是无论是添加删除还是判断都可以在O(1)时间复杂度内完成.

有一个需要注意的是当吃掉一个食物之后长度虽然增加了, 但是并不是即刻反应的, 也就是说如果当前一步吃掉了食物, 但是他所占的位置还没有增加, 
因为你不知道应该把长度添加在哪里. 所以需要一个标记, 在下一个指令给出的时候蛇的尾巴不移动, 只在移动方向上把这个长度加上.
"""
# http://blog.csdn.net/qq508618087/article/details/51756975
from collections import deque
class SnakeGame:
    
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.foods = deque(map(lambda a:tuple(a), food))
        self.snake = deque()
        self.snake.append((0, 0))
        self.W = width
        self.H = height

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        dirc = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        i, j = self.snake[-1]
        # print(i, j, self.foods[0], self.snake)
        di, dj = dirc[direction]
        ni, nj = i + di, j + dj
        # notice that the newHead can be equal to self.snake[0] (tail)
        if ni < 0 or ni >= self.H or nj < 0 or nj >= self.W or ((ni, nj) in self.snake and (ni, nj) != self.snake[0]):
            return -1
        if self.foods and (ni, nj) == self.foods[0]:
            self.snake.append((ni, nj))
            self.foods.popleft()
        else:
            self.snake.append((ni, nj))
            self.snake.popleft()
        return len(self.snake) - 1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


