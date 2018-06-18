#!/usr/bin/python
"""
我们用firstTurnBest(l, r)表示这一轮先取者能在COINS[l...r]上获得的最高分.
我们用secondTurnBest(l, r)表示这一轮后取者能在COINS[l...r]上获得的最高分.

举个例子, 假设一共有四枚硬币:[2,4,3,6], 那么:
firstTurnBest(1,2) = 4.因为在[2,4]中先取者最多能得到4分
secondTurnBest(1,2) = 2.因为在[2,4]中后取者最多能得到2分
firstTurnBest(2,4) = 9.因为在[4,3,6]中先取6,再取3
secondTurnBest(2,4) = 4.因为在[4,3,6]中后取者只能取到4

根据firstTurnBest和secondTurnBest的定义, 不难意识到:
SUM(l,r) = firstTurnBest(l,r) + secondTurnBest(l,r)
在这里, SUM(l,r) = COINS[l] + COINS[l+1] + ... + COINS[r]


假设一共有六枚硬币, 然后Alice先取, 那么Alice有两个选择: 她可以取第一枚也可以取第六枚.

如果她取走第1枚, 那下一轮就是Bob取, 所以她总共得到的分数是COINS[1] + SECOND_TURN_BEST(2, 6)
同理, 如果她取走第6枚, 那她能得到的总分是COINS[6] + SECOND_TURN_BEST(1, 5)
所以这一轮Alice最多能到的分数是刚刚两种情况的最大值:
firstTurnBest(1, 6) = max(COINS[1] + secondTurnBest(2, 6), COINS[6] + secondTurnBest(1, 5))

接下来我们讨论secondTurnBest. secondTurnBest记录的是如果下一轮取硬币者能得到的最大分数.
假设我们有六枚硬币, 但是我们要等Alice取完之后才能取, 那么我们能得到的最大分其实就是六枚的总和减去firstTurnBest(1,6):
secondTurnBest(1,6) = SUM(1, 6) - firstTurnBest(1, 6)

把刚才我们对firstTurnBest(1,6)的表达式代入,我们得到:
secondTurnBest(1,6) = SUM(1, 6) - (max(COINS[1] + secondTurnBest(2, 6), COINS[6] + secondTurnBest(1, 5)))
    = min(SUM(1,6) - COINS[1] - secondTurnBest(2,6),
              SUM(1,6) - COINS[6] - secondTurnBest(1,5))
    = min(SUM(2, 6) - secondTurnBest(2,6), SUM(1, 5) - secondTurnBest(1,5))
    = min(firstTurnBest(2, 6), firstTurnBest(1, 5))

理清了firstTurnBest和secondTurnBest的recursion关系, 我们上code:
"""
def max_score_double_recursive(points):
    def first_turn_best(left, right):
        if left == right:
            return points[left]
        return max(points[left] + second_turn_best(left + 1, right),
                   points[right] + second_turn_best(left, right - 1))

    def second_turn_best(left, right):
        if left == right:
            return 0
        return min(first_turn_best(left + 1, right), first_turn_best(left, right - 1))
    return first_turn_best(0, len(points) - 1)
"""
我们也可以把firstTurnBest和secondTurnBest写成一个函数: max_score_helper(my_turn, left, right). my_turn这个parameter就充当决定firstTurn还是secondTurn的角色:
"""
def max_score_recursive(points):
    def max_score_helper(my_turn, left, right):
        if left == right:
            return points[left] if my_turn else 0
        pick_head = max_score_helper(not my_turn, left + 1, right)
        pick_tail = max_score_helper(not my_turn, left, right - 1)
        if my_turn:
            return max(pick_head + points[left], pick_tail + points[right])
        else:
            return min(pick_head, pick_tail)
    return max_score_helper(True, 0, len(points) - 1)
"""
接下来我们看看能不能把my_turn这个parameter给去掉, 换句话说, 能不能用firstTurnBest自己来表示firstTurnBest从而把secondTurnBest这个函数给去掉

刚刚我们有:
firstTurnBest(1, 6) = max(COINS[1] + secondTurnBest(2, 6), COINS[6] + secondTurnBest(1, 5))
    = max(COINS[1] + min(firstTurnBest(3,6), firstTurnBest(2,5)), COINS[6] + min(firstTurnBest(1,4), firstTurnBest(2,5)))
好了, 我们成功地把firstTurnBest写成了关于自己的recursion:
"""
def first_turn_best(points):
    def first_turn_best_helper(left, right):
        if left == right:
            return points[left]
        if left == right - 1:
            return max(points[left:right+1])
        pick_head = min(first_turn_best_helper(left + 2, right),
                        first_turn_best_helper(left + 1, right - 1))
        pick_tail = min(first_turn_best_helper(left, right - 2),
                        first_turn_best_helper(left + 1, right - 1))
        return max(points[left] + pick_head, points[right] + pick_tail)
    return first_turn_best_helper(0, len(points) - 1)
"""
注意到在刚刚的firstTurnBest(1, 6)中, firstTurnBest(2,5)既出现在了取第一枚的情况中, 也出现在了取第六枚的情况中, 这意味着递归的解法会有重复计算, 所以我们采取一个简单的memoization:
"""
def first_turn_best_memoization(points):
    computed = {}

    def first_turn_best_helper(left, right):
        try:
            return computed[(left, right)]
        except KeyError:
            if left == right:
                return points[left]
            if left == right - 1:
                return max(points[left:right+1])
            pick_head = min(first_turn_best_helper(left + 2, right),
                            first_turn_best_helper(left + 1, right - 1))
            pick_tail = min(first_turn_best_helper(left, right - 2),
                            first_turn_best_helper(left + 1, right - 1))
            result = max(points[left] + pick_head, points[right] + pick_tail)
            computed[(left, right)] = result
            return result
    return first_turn_best_helper(0, len(points) - 1)

"""
既然能用memoization我们看看能不能用dynamic programming来实现. 在计算firstTurnBest(1, 6)时, 我们用到了firstTurnBest(1, 4), firstTurnBest(2, 5)和firstTurnBest(3, 6)
如果我们用一个n*n的矩阵来装firstTurnBest的话, opt[i][j]是由
opt[i][j-2], opt[i+1][j-1], opt[i+2][j]三项决定的.
由此可见, 我们在populate opt矩阵时需要先populate main diagonal([0,0], [1,1], [2,2], ...), 再populate diagonal上面一个diagonal([0,1], [1,2], [2,3], ...), 再populate [0,2], [1,3], [2,4], [3, 5], etc.
"""
def max_score_dp(points):
    size = len(points)
    opt = [[0 for _ in xrange(size)] for _ in xrange(size)]
    for gap in xrange(size):
        i, j = 0, gap
        while j < size:
            if i == j:
                opt[i][j] = points[i]
            elif i == j - 1:
                opt[i][j] = max(points[i:j+1])
            else:
                opt[i][j] = max(points[i] + min(opt[i+2][j], opt[i+1][j-1]),
                                points[j] + min(opt[i][j-2], opt[i+1][j-1]))
            i += 1
            j += 1
    return opt[0][-1]
