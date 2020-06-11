class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount+100]*(amount+1)
        dp[0] = 0
        for i in coins:
            if i < amount+1:
                dp[i] = 1
        for i in range(0, amount+1):
            for j in coins:
                if i > 0 and i <= amount and i-j > 0 and i-j < amount:
                    dp[i] = min(dp[i], dp[i-j]+1)
        if dp[i] == amount+100:
            return -1
        return dp[i]
