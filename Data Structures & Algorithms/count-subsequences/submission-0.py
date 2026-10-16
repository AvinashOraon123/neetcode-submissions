class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if m > n:
            return 0

        # dp[j] counts ways to form t[:j] from the processed part of s.
        dp = [0] * (m + 1)
        dp[0] = 1  # One way to form an empty target: select nothing.

        for i, char in enumerate(s):
            # Go backward so this source character is used at most once.
            for j in range(min(i + 1, m), 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
