class MinStack:

    def __init__(self):
        self.arr=[]


    def push(self, val: int) -> None:
        if len(self.arr)==0:
            return self.arr.append([val,val])
        mini=min(self.arr[-1][1],val)
        return self.arr.append([val,mini])
        

    def pop(self) -> None:
        if len(self.arr)==0:
            return -1
        return self.arr.pop()
        

    def top(self) -> int:
        if len(self.arr)==0:
            return -1
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()