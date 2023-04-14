# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []
        q = collections.deque()
        q.append(root)
        
        # using BFS
        while q:
            sub_arr = []
            for i in range(len(q)):
                node = q.popleft()
#                 non empty node append to sub_arr
#                  append righ and left node to queue
                if node:
                    sub_arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if sub_arr:
                res.append(sub_arr)
        return res
                    
                
        
        
            
            
        