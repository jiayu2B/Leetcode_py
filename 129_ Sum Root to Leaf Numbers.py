# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.DFS(root,0 )
    
    def DFS(self, root, presum):
        if root == None:
            return 0
        presum = presum*10 + root.val
        if root.right == None and root.left == None:
            return presum
        return self.DFS(root.right, presum) + self.DFS(root.left, presum)
