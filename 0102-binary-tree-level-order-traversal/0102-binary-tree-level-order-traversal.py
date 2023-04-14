# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

# recursive
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if not root:
            return 0
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)
        
########### BFS ############    
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res= []
#         q = collections.deque()
#         q.append(root)
        
#         # using BFS
#         while q:
#             sub_arr = []
#             for i in range(len(q)):
#                 node = q.popleft()
# #                 non empty node append to sub_arr
# #                  append righ and left node to queue
#                 if node:
#                     sub_arr.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if sub_arr:
#                 res.append(sub_arr)
#         return res
                    
                
        
        
            
            
        