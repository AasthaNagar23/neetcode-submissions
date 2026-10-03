class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            res=[]
            candidates.sort()
            def backtrack(i,curr,total):
                if total==target:
                    res.append(curr.copy())
                    return
                if total>target or i==len(candidates):
                    return
                for j in range(i,len(candidates)):
                    if j>i and candidates[j]==candidates[j-1]: #same level ke duplicates hatane ke liye use hua he 
                        continue
                    if total+candidates[j]>target: #if target cross ho jae
                        break
                    curr.append(candidates[j]) #choose
                    backtrack(j+1,curr,total+candidates[j]) #next element par repeat nahi hoga
                    curr.pop() #undo karo
            backtrack(0,[],0)
            return res
                    
                    