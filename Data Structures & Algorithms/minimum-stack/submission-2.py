class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins=[]
        self.out=[]
        self.ttop=-1
    def push(self, val: int) -> None:
        if self.ttop==-1:
            self.mins.append(val)
            self.ttop+=1
            self.stack.append(val)
        elif val< self.mins[self.ttop]:
            self.ttop+=1
            self.mins.append(val)
            self.stack.append(val)
        else:
            m= self.mins[self.ttop]
            self.ttop+=1
            self.mins.append(m)
            self.stack.append(val)

    def pop(self) -> None:
        self.ttop-=1
        self.mins.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[self.ttop]

    def getMin(self) -> int:
        return self.mins[self.ttop]
        
