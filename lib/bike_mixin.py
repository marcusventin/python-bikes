class BikeMixin:
    DEFAULT_CAPACITY = 20

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.bikes = []
        self.capacity = capacity

    def add(self, bike):
        if self.full():
            raise TypeError(f"This {type(self).__name__} can't "
            "take any more bikes.")
        else:
            self.bikes.append(bike)
    
    def remove(self, bike):
        self.bikes.remove(bike)
    
    def full(self):
        return(len(self.bikes) >= self.capacity)
    
    def empty(self):
        return(len(self.bikes) == 0)