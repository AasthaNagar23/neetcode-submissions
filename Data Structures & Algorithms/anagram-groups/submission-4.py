class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            a = ''.join(sorted(i))  #sorted(i)=like djfr ka [d,j,f,r] karta he 
            if a not in d:          #then use join karna hota he 
                d[a]=[]             #here d[a] ko hi ek aaray bana liya he 
            d[a].append(i)

        return list(d.values())


