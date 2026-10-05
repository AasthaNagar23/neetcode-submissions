class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        for i in nums1:
            if i not in arr:
                arr.append(i)
        for i in nums2:
            if i not in arr:
                arr.append(i)
        arr.sort()
        if len(arr)%2!=0:
            mid=len(arr)//2
            return float(arr[mid])
        else:
            mid=len(arr)//2
            return (arr[mid-1]+arr[mid])/2