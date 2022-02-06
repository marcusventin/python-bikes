from lib.bike_methods import BikeMethods

class RepairMan(BikeMethods):
    def collect_broken(self, docking_station):
        collect = [bike for bike in docking_station.bikes 
            if bike.working == False]
        
        for broken_bike in collect:
            self.add(broken_bike)
            broken_bike.release()
            docking_station.remove(broken_bike)

    def deliver_broken(self, garage):
        broken_bikes = [bike for bike in self.bikes if bike.working == False]

        for bike in broken_bikes:
            garage.add(bike)
            self.remove(bike)
    
    def collect_working(self, garage):
        collect = [bike for bike in garage.bikes if bike.working]

        for working_bike in collect:
            self.add(working_bike)
            garage.remove(working_bike)

    def deliver_working(self, docking_station):
        working_bikes = [bike for bike in self.bikes if bike.working]
        
        for bike in working_bikes:
            docking_station.add(bike)
            self.remove(bike)
            bike.dock()
