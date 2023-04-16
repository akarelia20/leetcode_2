# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # will need both in and pre order to construct tree
        
        if not preorder or not inorder:
            return
        
#        firstnode of preorder list will be a root node
        root = TreeNode(preorder[0])
    
#       mid will determine the index of root node in inorder list
        mid = inorder.index(preorder[0])
    
#       left node recursive call where preoder will exclude the root node (first node) upto the mid+1(because index starts form 0 in array), inorder will list of elements before root. 
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
#       preorder list of elements after left node and in inorder list elements after root node
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
        
        
            