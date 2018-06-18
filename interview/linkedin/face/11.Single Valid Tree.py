https://www.careercup.com/question?id=5103530547347456
import sets
class Solution(object):
    def isValid(self, nodes):
        s = set()
        #child node only has one parent
        for node in nodes:
            for child in [node.left, node.right]:
                if child != None:
                    if child in s:
                        return False
                    else:
                        s.add(child)
        #only one root node
        return len(nodes) - len(s) == 1     
s = Solution()