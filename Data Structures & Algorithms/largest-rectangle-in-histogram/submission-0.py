class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(len(heights)+1):
            if i==len(heights):
                curr=0
            else:
                curr=heights[i]
            while stack and curr<heights[stack[-1]]:
                h=heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    left=stack[-1]
                    width=i-stack[-1]-1
                area=width*h
                max_area=max(max_area,area)
            stack.append(i)
        return max_area