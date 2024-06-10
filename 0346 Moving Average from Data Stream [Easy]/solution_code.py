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