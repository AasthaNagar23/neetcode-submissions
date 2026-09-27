class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        curr=1
        ans=1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]-nums[i-1]==1:
                curr+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                curr=1
            ans=max(curr,ans)
        return ans
            