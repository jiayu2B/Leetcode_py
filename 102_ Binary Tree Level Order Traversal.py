# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preo(self, root, level):
        if root:
            if len(self.res) < level+1:
                self.res.append([])
            self.res[level].append(root.val)
            self.preo(root.left, level+1)
            self.preo(root.right, level+1)
    #两个函数，一个负责插入，一个主函数启动
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        self.preo(root, 0)
        return self.res
