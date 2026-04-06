class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity #preset storage


    def get(self, i: int) -> int:
        #empty check
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        #error check 
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.data[i] = n 


    def pushback(self, n: int) -> None:
        # if full, resize 
        if self.size >= self.capacity: 
            self.resize()
        self.data[self.size] = n
        self.size += 1


    def popback(self) -> int: 
        value = self.data[self.size - 1]
        self.data[self.size - 1] = None 
        self.size -= 1
        return value
 

    def resize(self) -> None:
        new_capacity = max(1, self.capacity *2) #doubles old
        new_data = [None]*new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
