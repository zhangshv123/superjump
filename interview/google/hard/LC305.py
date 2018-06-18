class Solution(object):
    
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        islandNum = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        union_map = {}
        res = []
        for pos in positions:
            val = pos[0] * n + pos[1]
            union_map[val] = val
            islandNum += 1
            for dir in directions:
                newX = pos[0] + dir[0]
                newY = pos[1] + dir[1]
                newVal = newX * n + newY
                if newX >=0 and newX < m and newY >=0 and newY < n and newVal in union_map:
                    if self.union(val, newVal, union_map):
                        islandNum -= 1
            res.append(islandNum)
        return res
        
    def union(self, m, n, union_map):
        parent_m = self.find(m, union_map)
        parent_n = self.find(n, union_map)
        if parent_m == parent_n:
            return False
        union_map[parent_m] = parent_n
        return True
        
    def find(self, n, union_map):
        if n == union_map[n]:
            return n
        parent = union_map[n]
        # shink the map
        union_map[n] = union_map[parent]
        return self.find(parent, union_map)