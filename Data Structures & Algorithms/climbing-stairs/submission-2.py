class Solution:
    def climbStairs(self, n: int) -> int:
        #memoization (Top Down DP)
        memo = {}
        def solve(step):
            if step == 1:
                return 1
            if step == 2:
                return 2

            if step in memo:
                return memo[step]
            memo[step] = solve(step - 1) + solve(step - 2)
            return memo[step]
        return solve(n)