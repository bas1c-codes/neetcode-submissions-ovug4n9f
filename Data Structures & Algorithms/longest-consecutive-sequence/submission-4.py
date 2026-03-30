class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
                s=set(nums)
                #mini = min(s)
                co=[]
                l=[]
                for i in nums:
                        if i-1 not in s:
                                l.append(i)
                        else:
                                continue
                if l ==[]:
                        return 0
                for i in l:# starting point eduth
                        #expand cheyn vendi rand var venam onn counter rand current elem for exapnsion
                        cur = i
                        c=1
                        while cur+1 in s:
                                c+=1
                                cur+=1
                        co.append(c)
                return max(co)

                