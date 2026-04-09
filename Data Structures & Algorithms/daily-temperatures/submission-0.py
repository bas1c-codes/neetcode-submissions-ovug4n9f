class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ind=[]
        stack=[]
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
           
            while ind and temperatures[i]>temperatures[ind[-1]]:
                prev = ind.pop()
                result[prev] = i-prev
                    #stack.append(i-ind.pop())
            ind.append(i)
        return result
                
        