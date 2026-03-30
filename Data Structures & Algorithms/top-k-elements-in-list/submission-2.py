class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= Counter(nums)
        l=[]
        for _ in range(k): # we loop in k [0,1]
            n = max(d,key=d.get) #
            l.append(n)
            d.pop(n)
        return l