class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j= len(heights)-1
        m=0
        while i<j:
            height = min(heights[i],heights[j])
            width=j-i
            m = max(m,height*width)
            if heights[i] <heights[j]:
                i+=1
            else:
                j-=1
        return m
        