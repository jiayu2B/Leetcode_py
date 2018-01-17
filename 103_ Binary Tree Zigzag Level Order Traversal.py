# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.applist(root, 0)
        for i in range(0,len(self.res)):
            if i%2 == 1:
                self.res[i] = self.res[i][::-1]
        return self.res
        
    def applist(self, root, level):
        #if root是必须的
        if root:
            if len(self.res) < level+1:
                self.res.append([])
            self.res[level].append(root.val)
            self.applist(root.left,level+1)
            self.applist(root.right,level+1)
        
