#一个中国小哥哥，人特好，binary tree， 找max difference（必须是有上下级关系的两个node，不能是同级的）， 分治法
#!/usr/bin/python
def maxDiff(root):
	def dfs(root, minV, maxV):
		if root is None:
			return 0
		left = dfs(root.left, min(minV, root.val), max(maxV, root.val))
		right = dfs(root.right, min(minV, root.val), max(maxV, root.val))
		return max(left, right, abs(root.val - minV), abs(root.val - maxV))