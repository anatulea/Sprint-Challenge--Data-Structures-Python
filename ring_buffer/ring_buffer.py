class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer_storage = []
        self.oldest_index = 0

    def append(self, item):
        # Check if the buffer list is smaller then the capacity
        if len(self.buffer_storage) < self.capacity:
            # Append the item to the end of the list
            self.buffer_storage.append(item)
        # else if the buffer list is not smaller than the capacity    
        else:
            # set new item to replace the list element with the oldest index
            self.buffer_storage[self.oldest_index] = item
           
           # if the oldest index is smaller than the buffer list length -1
            if self.oldest_index < len(self.buffer_storage)-1:
                # increase the oldest index by one
                self.oldest_index += 1
            # else if if the oldes index is  larger than the buffer list length -1
            else:
                # set the oldest intex to 0
                self.oldest_index = 0  

    def get(self):
        # returns the whole buffer storage list
        return self.buffer_storage

buffer = RingBuffer(3)
buffer.append('one')
buffer.append('two')
buffer.append('three')
print(buffer.get())
# ['one', 'two', 'three']
buffer.append('four')
print(buffer.get())
# ['four', 'two', 'three']
buffer.append('five')
print(buffer.get())
# ['four', 'five', 'three']
buffer.append('one2')
buffer.append('two2')
buffer.append('three2')
print(buffer.get())
