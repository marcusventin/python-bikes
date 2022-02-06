from lib.bike_methods import BikeMethods

class DockingStation(BikeMethods):
    def release_bike(self):
        working_bikes = [bike for bike in self.bikes if bike.working]
        if len(working_bikes) == 0:
            raise IndexError("There are no working bikes in this station.")
        else:
            bike = working_bikes[0]
            self.remove(bike)
            bike.release()
    
    def dock(self, bike):
        self.add(bike)
        bike.dock()
    

