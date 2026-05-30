class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        l = 0
        r = len(arr)-1
        maxs = -1
        while l<=r:
            mid = (l+r)//2
            if timestamp >= arr[mid][0]:
                maxs = mid
                l = mid+1
            else: # else means arr > time stamp so dont recode the value here
                #maxs = max(maxs,mid)
                r=mid-1
        if maxs == -1:
            return ""
        return arr[maxs][1]

