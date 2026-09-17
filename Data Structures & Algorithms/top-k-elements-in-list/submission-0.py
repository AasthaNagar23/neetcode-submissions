class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        result = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        m=[]
        count=0
        for i in result:
            m.append(i)
            count+=1
            if count==k:
                break
        return m