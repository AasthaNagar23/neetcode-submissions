class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        e=[]
        for i in range(n+1):
            x=i
            b=[]
            while x>0:
                a=x%2
                b.append(a)
                x=x//2
            d=0
            for j in b:
                d+=j
            result.append(d)
        return result
