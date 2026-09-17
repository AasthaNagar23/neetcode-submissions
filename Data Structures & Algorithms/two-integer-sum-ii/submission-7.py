class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while low<high:
            mid = numbers[low]+numbers[high]
            if target==mid:
                return [low+1,high+1]
            elif mid<target:
                low+=1
            else:
                high-=1

