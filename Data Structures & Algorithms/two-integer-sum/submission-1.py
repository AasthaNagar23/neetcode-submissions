class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    d.append([i,j])
                    
        for i in d:
            return i
        return -1