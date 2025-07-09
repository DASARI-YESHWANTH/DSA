class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Function to push an element x in a queue.
    def push(self, x):
        self.stack1.append(x)

    # Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()
