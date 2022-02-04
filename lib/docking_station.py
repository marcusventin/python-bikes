from lib.bike import Bike

class DockingStation:
    def __init__(self):
        self.bikes = []
    
    def release_bike(self, bike):
        self.bikes[-1].release()