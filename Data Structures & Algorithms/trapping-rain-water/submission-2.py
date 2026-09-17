class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        water=0
        for num in range(len(height)):
            while stack and height[stack[-1]]<height[num]:
                bottom=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                width=num-left-1
                h=min(height[left],height[num])-height[bottom]
                water+=h*width
            stack.append(num)
        return water