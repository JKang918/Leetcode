## 232. Implement Queue using Stacks

>Description: [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)\
Check out the link above for detailed description.\
A short version: replicate features of queue using two stacks.

Constraints:

- All the calls to `pop` and `peek` are valid.
- <code>1 <= x <= 9</code> 
- At most 100 calls will be made to `push`, `pop`, `peek`, and `empty`.

### Solution: 

```python
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
```
### Breakdown of Solution:

The class has two stack members.

The member function `push` is the core of the solution. 

Basically, when elements are pushed into `MyQueue`, using two stacks, we reverse the order the data are stored.

- pop each element in a stack that is not empty to the other one.
- pop each element in the previously empty one to the original one.

The above is how you reverse the order.

If we store data like that, then for `pop` and `peek` functions, we can simply use pre-stored `pop` and `peek` fucntions for python stack. 


### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the number of elements to push, pop, peek

Space Complexity: *O(n)*

- linearly correlated with the number of elements to push, pop, peek