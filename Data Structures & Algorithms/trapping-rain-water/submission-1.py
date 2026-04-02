class Solution:
    def trap(self, height: List[int]) -> int:
        max_l,max_r=0,0
        n = len(height)
        l_wall = [0]*n
        r_wall = [0]*n
        for i in range(n):
            j = -i-1
            l_wall[i]=max_l
            r_wall[j]=max_r
            max_l=max(max_l,height[i])
            max_r=max(max_r,height[j])
        s=0
        for i in range(n):
            pot = min(l_wall[i],r_wall[i])
            s+=max(0,pot-height[i])
        return s

            
            
        