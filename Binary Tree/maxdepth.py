## maximum depth of a binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#given input =[3,9,20,null,null,15,7] ->3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_depth=self.maxDepth(root.left)
            right_depth=self.maxDepth(root.right)
            
            if(left_depth>right_depth):
                return left_depth+1
            else:
                return right_depth+1