class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        a = [1]*len(nums)
        for i in range(1,len(nums)):
            # make the product of each number in a way theat its the product of the number before <-
            a[i] = a[i-1]*nums[i-1]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            
            a[i] = right * a[i]
            right = right*nums[i]
        return a