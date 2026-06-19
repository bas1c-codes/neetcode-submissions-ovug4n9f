class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        i=0
        j=0
        m=0
        min_len = float("inf")
        start = 0
        while j <len(s):
            ch = s[j]
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch]<=need[ch]:
                m+=1
            while m==len(t):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    start = i
                window[s[i]]-=1
                if s[i] in need and window[s[i]]<need[s[i]]:
                    m-=1
                i+=1
            j+=1
        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
            
            
                 