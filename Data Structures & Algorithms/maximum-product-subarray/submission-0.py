class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min=nums[0]
        curr_max=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            a=nums[i]
            if a<0:
                curr_min,curr_max=curr_max,curr_min
            curr_min=min(a,curr_min*a)
            curr_max=max(a,curr_max*a)
            result=max(result,curr_max)
        return result