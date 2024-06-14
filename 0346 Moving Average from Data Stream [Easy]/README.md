## 346. Moving Average from Data Stream

>Description: [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)\
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.\
Implement the MovingAverage class:
- `MovingAverage(int size)` Initializes the object with the size of the window `size`.
- `double next(int val)` Returns the moving average of the last `size` values of the stream.


Constraints:

- <code>1 <= size <= 1000</code>
- <code>-10<sup>5</sup> <= val <= 10<sup>5</sup></code> 
- At most 10<sup>4</sup> calls will be made to next.


### Solution: 

```python
class MovingAverage:
    #concept of circular queue
    def __init__(self, size: int):
        self.queue = [None] * size
        self.size  = size
        self.ptr = 0
        self.movsum = 0   #moving sum


    def next(self, val: int) -> float:
       
        if self.queue[self.ptr] is not None:        #circular queue
            self.movsum -= self.queue[self.ptr]     #when came full circle -> first remove that value in place
        
        self.queue[self.ptr] = val
        self.movsum += val
        self.ptr = (self.ptr + 1) % self.size       #circular queue
       
        if self.queue[self.ptr] is None:            #when the fixed size array is not full
            return self.movsum / self.ptr
        else:                                       #when the pointer came full circle (= the fixed size array is full)
            return self.movsum / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

```
### Breakdown of Solution:

**Circular Queue**

Queue or deque can also be used, but I chose to use circular queue because it allows to use just a single pointer in this particular question.

I added an attribute, `movsum` to **avoid using sum method for array (in python, list)**.

Below is the breakdown of how the moving average is calculated: (*suppose the size of circular queue is 5*)

1. Enqueue to `queue[0]` and move the pointer to `1`. The moving sum is the input value. (First `if` block not run)
2. The moving average is `queue[0]` / `1`, `1` being the same value as the pointer. Hence `self.movsum / self.ptr`.

Whenever the member function, `next` is called, 1. and 2. are repeated until the queue is full. Below is when the last value is put and the pointer comes full circle.

1. Enqueue to `queue[4]` and move the pointer to `0` (**<- modular operation**). The moving sum is the cumulative sum of the all elements. (First `if` block not run)
2. The moving average is `queue[0]` / `5`, `5` being the `size` of the queue. Hence `self.movsum / self.size` (Last `else` block is run).
3. Enqueue to `queue[0]` and move the pointer to `0`. But before this, the first `if` block is run to subtract the previous value in the place of `queue[0]` from the moving sum before overwritten. 
4. The moving average is `queue[0]` / `5`, `5` being the `size` of the queue. Hence `self.movsum / self.size` (Last `else` block is run).
5. The same process goes on so forth

### Complexity Analysis:

Time Complexity: *O(1)*

- overwrite whtere the pointer is pointing at

Space Complexity: *O(n)*

- store the circular queue
    
