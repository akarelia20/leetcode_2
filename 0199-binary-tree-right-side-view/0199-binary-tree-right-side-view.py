# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,0,res)
        return res
        
    def helper(self, root,depth, res):
        if not root:
            return 0
# if len is 3 and depth is 3 (meaning level 4 because depth starts at 0) then it needs append 1 more element to res.
        if len(res) == depth:
            res.append(root.val)
        self.helper(root.right, depth+1, res)
        self.helper(root.left, depth+1, res)