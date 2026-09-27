class Solution:
    def hammingWeight(self, n: int) -> int:
        b=[]
        count=0
        while n>0:
            a=n%2
            b.append(a)
            n=n//2
        for i in b:
            if i==1:
                count+=1
        return count
