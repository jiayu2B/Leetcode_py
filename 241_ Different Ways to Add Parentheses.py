class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit(): return [int(input)]
        #判断是否为数字
        res = []
        for i in range(0,len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i+1::])
                #分治法，找到一个操作符后计算左右侧所有组合。
                for l in left:
                    for r in right:
                        res.append(eval(str(l)+input[i]+str(r)))
                        #将所有组合运算出来
        return res
    
