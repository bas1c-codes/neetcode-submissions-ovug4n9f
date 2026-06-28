class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        d=None
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        d =0
        while slow!=d:
            slow = nums[slow]
            d = nums[d]
        return d

        