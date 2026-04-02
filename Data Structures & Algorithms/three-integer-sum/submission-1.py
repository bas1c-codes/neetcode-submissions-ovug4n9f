class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums =sorted(nums)
        l=[]
        for c in range(len(nums)):
            if c>0 and nums[c]==nums[c-1]:
                continue
            i=c+1
            j=len(nums)-1
            cur=nums[c]
            while i<j:
                if cur+nums[i]+nums[j]<0:
                    i+=1
                elif cur+nums[i]+nums[j]>0:
                    j-=1
                else:
                    l.append([cur,nums[i],nums[j]])
                    i+=1
                    j-=1

                    # 🔴 2. Skip duplicate i
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                    # 🔴 3. Skip duplicate j
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return l