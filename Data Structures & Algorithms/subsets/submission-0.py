class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new_subsets=[]
            for subset in res:
                new=subset+[num]
                new_subsets.append(new)
            res+=new_subsets
        return res

