class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z= target
        a=False
        b=False
        c=False
        for i in triplets:
            if i[0]>x or i[1]>y or i[2]>z:
                continue
            if i[0]==x:
                a=True
            if i[1]==y:
                b=True
            if i[2]==z:
                c=True
        return a and b and c
            
