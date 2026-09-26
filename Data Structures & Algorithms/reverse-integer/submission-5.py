class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            a=str(x)
            b=a[::-1]
            c=int(b)
            if c>(2**31-1):  #don't use ^, use ** this
                return 0
            return c

        else:
            a=-(x)
            b=str(a)
            c=b[::-1]
            d=-(int(c))
            if d<(-2**31):
                return 0
            return d