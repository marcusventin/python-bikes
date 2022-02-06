from lib.bike_methods import BikeMethods

class DockingStation(BikeMethods):
    def release_bike(self):
        working_bikes = [bike for bike in self.bikes if bike.working]
        
        if len(working_bikes) == 0:
            raise IndexError("There are no working bikes in this station.")
        else:
            bike = working_bikes[0]
            bike.release()
            self.remove(bike)
    
    def dock(self, bike):
        if self.full():
            raise TypeError("This station is full")
        else:
            bike.dock()
            self.add(bike)
    

