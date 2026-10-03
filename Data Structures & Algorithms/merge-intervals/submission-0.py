class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        for start,end in intervals:
            if not result:
                result.append([start,end])
            elif start<=result[-1][1]:
                result[-1][1]=max(result[-1][1],end)
            else:
                result.append([start,end])
        return result