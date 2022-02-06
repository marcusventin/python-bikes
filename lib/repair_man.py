class RepairMan:
    def __init__(self):
        self.bikes = []

    def collect_broken(self, docking_station):
        self.collect = [bike for bike in docking_station.bikes 
            if bike.working == False]
        
        for broken_bike in self.collect:
            self.bikes.append(broken_bike)
        self.collect.clear()

        docking_station.remove_broken()