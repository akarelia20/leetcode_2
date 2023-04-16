# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        def dfs(root):
        
            if not root or len(stack) > k:
                return 0

            if root.left:
                dfs(root.left)
            if stack and stack[-1] > root.val:
                temp= stack[-1]
                stack[-1] = root.val
                stack.append(temp)
            else:
                stack.append(root.val) 
            if root.right:
                dfs(root.right)
                
            
            print(root.val, stack)
            
            
            
            
        dfs(root)    
        return stack[k-1]
                