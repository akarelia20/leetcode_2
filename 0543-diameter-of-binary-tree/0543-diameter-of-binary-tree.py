# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            res = max (res, right + left) # updates max diameter
            return 1 + max(left,right)  #gives the height at the root node at every recursive call
        dfs(root)  
        return res