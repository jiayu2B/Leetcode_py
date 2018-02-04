# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if abs(self.Height(root.right) - self.Height(root.left)) <= 1:
        #一旦有一个位置不满足，则return False
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False
            
    #一个找高度的函数
    def Height(self, root):
        if root == None:
            return 0
        else:
            return max(self.Height(root.right), self.Height(root.left))+1
        
