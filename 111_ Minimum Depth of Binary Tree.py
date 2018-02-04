# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        #一旦有一边为None，则不看这一边。
        if root.left == None and root.right != None:
            return self.minDepth(root.right)+1
        elif root.right == None and root.left != None:
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.right),self.minDepth(root.left))+1
        
