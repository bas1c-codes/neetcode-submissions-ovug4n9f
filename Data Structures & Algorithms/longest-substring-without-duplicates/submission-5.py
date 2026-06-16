class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        k=0
        if len(s)==0:
            return 0
        l=s[0]
        if len(s)==1:
            return 1
        while i<len(s) and j<len(s):
            if s[j] not in l:
                l = l+s[j]
                j+=1
            else:
                k = max(k,len(l))
                l=l[1:]
                i+=1
               # j=i+1
        k = max(k, len(l))
        return k

        
        