from lib.bike import Bike

class DockingStation:
    def __init__(self):
        self.bikes = []
    
    def release_bike(self):
        for bike in self.bikes:
            if bike.working:
                bike.release()
                self.bikes.remove(bike)
                break