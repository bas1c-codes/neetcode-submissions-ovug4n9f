class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i=0
        c=0
        j=len(s1)-1
        while j<len(s2):
            if Counter(s2[i:j+1])==Counter(s1):
                return True
            else:
                i+=1
                j+=1
        return False
        