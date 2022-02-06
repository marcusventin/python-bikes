from lib.bike import Bike

class DockingStation:
    DEFAULT_CAPACITY = 20

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.bikes = []
        self.capacity = capacity
    
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
    
    def remove_broken(self):
        broken_bikes = [bike for bike in self.bikes 
            if bike.working == False]
        while broken_bikes:
            self.bikes.remove(broken_bikes.pop())

    def accept_working(self, working_bikes):
        for bike in working_bikes:
            self.bikes.append(bike)


    def full(self):
        return(len(self.bikes) >= self.capacity)
    
    def empty(self):
        return(len(self.bikes) == 0)
    

