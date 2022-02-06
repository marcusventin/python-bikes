class Garage:
    DEFAULT_CAPACITY = 20

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.bikes = []
        self.capacity = capacity
    
    def full(self):
        return(len(self.bikes) >= self.capacity)