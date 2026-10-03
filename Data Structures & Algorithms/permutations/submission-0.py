class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used = [False]*(len(nums))
        def backtrack(curr):
            if len(nums)==len(curr):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                curr.append(nums[i])  #choosing
                used[i]=True
                backtrack(curr)    #next position
                curr.pop()            #undo
                used[i]=False  
        backtrack([])
        return res