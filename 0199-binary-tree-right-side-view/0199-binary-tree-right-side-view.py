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
#         rightnodes will be appended until it is present but if right side has depth of 5 and left is with depth of 6 then it will append 5 right nodes and last (6th)node will be left node
# order of recursive call matters , call right recursive function first
        if len(res) == depth:
            res.append(root.val)
        self.helper(root.right, depth+1, res)
        self.helper(root.left, depth+1, res)