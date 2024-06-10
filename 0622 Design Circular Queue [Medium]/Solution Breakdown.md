## 622. Design Circular Queue

>Description: [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)\
Check the link for detailed instructions.


Constraints:

- <code>1 <= k <= 1000</code>
- <code>1 <= value <= 1000</code> 
- At most `3000` calls will be made to `enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, and `isFull`.


### Solution: 

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k                    #fixed-size array
        self.size  = k                          #size of the queue
        self.head  = 0                          #head pointer for dequeue
        self.tail  = 0                          #tail pointer for enqueue
        self.count = 0                          #if count == size: full
       
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
       
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size     #"circular" queue 
        self.count += 1
        return True
       


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
       
        self.queue[self.head] = 0
        self.head = (self.head + 1) % self.size     #"circular" queue
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1                  # given condition
        return self.queue[self.head]
       
    def Rear(self) -> int:
        if self.isEmpty():
            return -1                  # given condition
        return self.queue[self.tail - 1]
       
    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
       
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

```
### Breakdown of Solution:

**Circular Queue**

Circular Queue can be realized with using fixed size array.

The most important takeaway is the usage of modular operations in enqueue and dequeue functions. 

When the tail pointer reaches the end of the fixed size array, it goes back to the first element of array and do the job there.

### Complexity Analysis:

N/A