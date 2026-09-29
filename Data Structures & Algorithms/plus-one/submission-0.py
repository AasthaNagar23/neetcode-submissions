class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=""
        res1=[]
        for i in digits:
            b=str(i)
            c+=b
        d=int(c)
        res=d+1
        for i in str(res):
            res1.append(int(i))
        return res1
