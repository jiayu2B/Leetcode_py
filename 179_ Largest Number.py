class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted([str(x) for x in nums], cmp = self.com)
        ans = ''.join(nums).lstrip('0')
        return ans or '0'
    #按照连接后大小来排序，将连接后最大的排在最前面
    def com(self, a, b):
        return int(b+a) - int(a+b)
