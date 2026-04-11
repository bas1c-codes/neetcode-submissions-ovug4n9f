class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i],speed[i])  for i in range(len(speed))]
        f=0
        curtime = 0
        for position,speed in sorted(pairs,reverse=True):
            destination_time = (target-position)/speed
            if curtime<destination_time:
                f+=1
                curtime = destination_time
        return f
        