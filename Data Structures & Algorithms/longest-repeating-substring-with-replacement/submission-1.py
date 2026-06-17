class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        i=0
        j=0
        n=0
        win=0
        maxFreq=0
        res=0
        while j<len(s):
            if s[j] not in d:
                d[s[j]]=1
            else:
                d[s[j]]+=1
            win = j-i+1
            maxFreq = max(maxFreq, d[s[j]])
            n = win-maxFreq
            if n <=k:
                j+=1
                res=max(res,win)
            else:
                d[s[i]]-=1
                i+=1
                j+=1
                
            
        return res