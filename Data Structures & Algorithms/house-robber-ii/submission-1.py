class Solution:
    def rob(self, nums: List[int]) -> int:
        m=len(nums)
        if m==0:
            return 0
        if m==1:
            return nums[0]
        def house_rob(arr):
            n=len(arr)
            if n==0:
                return 0
            if n==1:
                return arr[0]
            dp=[0]*(n+1)
            dp[0]=0
            dp[1]=arr[0]
            for i in range(2,n+1):
                take=dp[i-2]+arr[i-1]
                skip=dp[i-1]
                dp[i]=max(take,skip)
            return dp[n]
        case1=house_rob(nums[:-1])
        case2=house_rob(nums[1:])
        return max(case1,case2)
