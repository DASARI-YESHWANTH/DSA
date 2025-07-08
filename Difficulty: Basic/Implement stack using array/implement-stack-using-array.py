class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        return self.arr.append(data)
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if len(self.arr)==0:
            return -1
        return self.arr.pop()
        
        