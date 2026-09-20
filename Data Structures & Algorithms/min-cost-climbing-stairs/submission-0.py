class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=0
        for i in range(2,n+1):
            a=dp[i-1]+cost[i-1]
            b=dp[i-2]+cost[i-2]
            dp[i]=min(a,b)
        return dp[n]