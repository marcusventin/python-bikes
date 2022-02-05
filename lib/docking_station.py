from lib.bike import Bike

class DockingStation:
    def __init__(self):
        self.bikes = []
    
    def release_bike(self):
        if len(self.bikes) == 0:
            raise IndexError("There are no bikes in this station")
        else:
            for bike in self.bikes:
                if bike.working:
                    bike.release()
                    self.bikes.remove(bike)
                    break
    
    def dock(self, bike):
        bike.dock()
        self.bikes.append(bike)
        