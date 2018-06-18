"""

Equations are given in the format A / B = k, where A and B are variables represented as strings,
 and k is a real number (floating point number). Given some queries, return the answers. 
 If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> 
queries , where equations.size() == values.size(), and the values are positive. This represents the equations. 
Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
"""

"""
A series of equations A / B = k can be seen as a graph in which nodes are the dividend and divisor A and B
 and weights are the result of the division. So we simply create the graph and traverse it with DFS/BFS to get our result.

Complexity is K * O(N + M) where N and M are the number of nodes and edges, and K is the number of queries. 
How many nodes can we have? It’s 2 * E, where E is the number of equations (2 different nodes per each equation). 
We can have at most E edges in the graph.

So total complexity is O(K * E), with O(E) additional space for the graph.
"""
from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        G, W = defaultdict(set), defaultdict(float)
        for (a, b), v in zip(equations, values):
            G[a].add(b)
            G[b].add(a)
            W[a, b], W[b, a] = v, 1.0 / v
        def dfs(start, end, path):
            if start == end and start in G:
                nonlocal ans
                ans = path
                return
            if start in visited:
                return
            visited.add(start)
            for c in G[start]:
                dfs(c, end, path * W[start, c])
        res = []
        for a, b in queries:
            visited, ans = set(), -1.0
            dfs(a, b, 1)
            res.append(ans)
        return res
"""
Floyd–Warshall
https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
A variation of Floyd–Warshall, computing quotients instead of shortest paths. An equation A/B=k 
is like a graph edge A->B, and (A/B)*(B/C)*(C/D) is like the path A->B->C->D.
"""
def calcEquation(self, equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k, i, j in itertools.permutations(quot, 3):
        if k in quot[i] and j in quot[k]:
            quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]
