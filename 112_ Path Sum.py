# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, _sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.right == None and root.left == None:
            return root.val == _sum
        #题目是要看有没有一条线能够达到sum
        else:
            return self.hasPathSum(root.right,_sum-root.val) or self.hasPathSum(root.left, _sum-root.val)
