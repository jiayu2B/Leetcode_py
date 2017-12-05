class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.valid(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.valid(col):
                return False
        
        for i in (0,3,6):
            for j in (0,3,6):
                block = [board[t1][t2] for t1 in (i,i+1,i+2) for t2 in (j,j+1,j+2)]
                if not self.valid(block):
                    return False
        return True
        
    def valid(self, list):
        map = {}
        for i in list:
            if i != ".":
                if i in map:
                    return False
                else:
                    map[i] = True
        return True
