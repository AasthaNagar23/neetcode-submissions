class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res


    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=s.index("#",i) #i ke position ke baad wala pehla # kis position par he right
            n=int(s[i:j]) # ye "5" ko 5 mein convert karta he 
            word=s[j+1:j+1+n]
            result.append(word)
            i=j+1+n
        return result
