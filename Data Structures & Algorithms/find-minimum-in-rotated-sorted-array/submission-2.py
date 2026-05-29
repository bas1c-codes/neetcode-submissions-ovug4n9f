class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        k=0
        d=0
        while l<=r:
            mid = (l+r)//2
            if nums[r]<=nums[mid]:
                l=mid+1
            else:
                r=mid
            k=mid
        return min(nums[k],nums[d])
        
        