class RepairMan:
    def __init__(self):
        self.bikes = []

    def collect_broken(self, docking_station):
        collect = [bike for bike in docking_station.bikes 
            if bike.working == False]
        
        for broken_bike in collect:
            self.bikes.append(broken_bike)
            broken_bike.release
        collect.clear()

        docking_station.remove_broken()
    
    def deliver_broken(self, garage):
        broken_bikes = [bike for bike in self.bikes if bike.working == False]

        garage.accept(broken_bikes)
        
        while broken_bikes:
            self.bikes.remove(broken_bikes.pop())
    
    def collect_working(self, garage):
        collect = [bike for bike in garage.bikes if bike.working]

        while collect:
            self.bikes.append(collect.pop())
        
        garage.despatch_working()

    def deliver_working(self, docking_station):
        working_bikes = [bike for bike in self.bikes if bike.working]
        
        docking_station.accept_working(working_bikes)

        while working_bikes:
            self.bikes.remove(working_bikes.pop())


