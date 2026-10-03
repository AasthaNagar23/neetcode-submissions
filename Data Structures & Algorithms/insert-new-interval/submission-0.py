class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        start, end= newInterval
        for idx, (i,j) in enumerate(intervals):
            if j<start:
                result.append([i,j])
            elif i>end:
                result.append([start,end])
                result.append([i,j])
                result.extend(intervals[idx+1:])
                return result
            else:
                start=min(start,i)
                end=max(end,j)
        result.append([start,end])
        return result