class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) #now target is empty
        
            self.stack1.append(x)
            #make emptystack empty agian
            while self.stack2:
                self.stack1.append(self.stack2.pop()) #now emptystack is empty

        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop()) #now target is empty
        
            self.stack2.append(x)
            #make emptystack empty agian
            while self.stack1:
                self.stack2.append(self.stack1.pop()) #now emptystack is empty

    def pop(self) -> int:
        if not self.stack2:
            return self.stack1.pop()
        if not self.stack1:
            return self.stack2.pop()
               

    def peek(self) -> int:
        if not self.stack2:
            return self.stack1[-1]
        if not self.stack1:
            return self.stack2[-1]
       

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()