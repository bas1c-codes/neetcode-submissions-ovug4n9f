class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        if len(numbers)==2:
            return [1,2]
        elif j==0:
            return []
        while i<j:
            s = numbers[i]+numbers[j]
            print(s)
            if s==target:
                return [i+1,j+1]
            elif s<target:
                i+=1
            elif s>target:
                j-=1
        
