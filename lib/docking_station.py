from lib.bike import Bike

class DockingStation:
    def __init__(self):
        self.bikes = []
        self.default_capacity = 20
    
    def release_bike(self):
        if self.empty():
            raise IndexError("There are no bikes in this station")
        else:
            for bike in self.bikes:
                if bike.working:
                    bike.release()
                    self.bikes.remove(bike)
                    break
    
    def dock(self, bike):
        if self.full():
            raise TypeError("This station is full")
        else:
            bike.dock()
            self.bikes.append(bike)
    
    def full(self):
        return(len(self.bikes) >= self.default_capacity)
    
    def empty(self):
        return(len(self.bikes) == 0)
    

