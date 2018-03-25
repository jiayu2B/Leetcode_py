class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        self.helper(res, root, 0)
        return res
    
    def helper(self, res, root, level):
        if root == None:
            return
        if len(res) == level:
            res.append(root.val)
        self.helper(res, root.right, level+1)
        self.helper(res, root.left, level+1)
        
