class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        d=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            l=int(s[i:j])
            word=s[j+1:j+1+l]
            d.append(word)
            i=j+l+1
        return d
