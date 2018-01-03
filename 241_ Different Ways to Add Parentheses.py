class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit(): return [int(input)]
        
        res = []
        for i in range(0,len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i+1::])
                for l in left:
                    for r in right:
                        res.append(eval(str(l)+input[i]+str(r)))
        return res
    
