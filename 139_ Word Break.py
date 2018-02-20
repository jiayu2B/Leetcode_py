class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                #如果dp的j位置也是True，且Dict中存在字符串，那么该位置为True
                    dp[i] = True
        return dp[len(s)]
