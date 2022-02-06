from lib.bike_methods import BikeMethods

class RepairMan(BikeMethods):
    def collect_broken(self, docking_station):
        collect = [bike for bike in docking_station.bikes 
            if bike.working == False]
        
        for broken_bike in collect:
            if self.full():
                raise TypeError("This repairman can't take any more!")
            else:
                self.add(broken_bike)
                broken_bike.release()
                docking_station.remove(broken_bike)
        collect.clear()

    def deliver_broken(self, garage):
        broken_bikes = [bike for bike in self.bikes if bike.working == False]

        for bike in broken_bikes:
            if garage.full():
                raise TypeError("This garage is full")
            else:
                garage.add(bike)
                self.remove(bike)
    
    def collect_working(self, garage):
        collect = [bike for bike in garage.bikes if bike.working]

        for working_bike in collect:
            if self.full():
                raise TypeError("This repairman can't take any more!")
            else:
                self.add(working_bike)
                garage.remove(working_bike)

    def deliver_working(self, docking_station):
        working_bikes = [bike for bike in self.bikes if bike.working]
        
        for bike in working_bikes:
            if docking_station.full():
                raise TypeError("This station is full")
            else:
                docking_station.add(bike)
                self.remove(bike)
                bike.dock()


