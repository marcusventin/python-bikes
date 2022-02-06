class RepairMan:
    DEFAULT_CAPACITY = 20

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.bikes = []
        self.capacity = capacity

    def collect_broken(self, docking_station):
        collect = [bike for bike in docking_station.bikes 
            if bike.working == False]
        
        for broken_bike in collect:
            if self.full():
                raise TypeError("This repairman can't take any more!")
            else:
                self.bikes.append(broken_bike)
                broken_bike.release
                docking_station.bikes.remove(broken_bike)
        collect.clear()

    def deliver_broken(self, garage):
        broken_bikes = [bike for bike in self.bikes if bike.working == False]

        for bike in broken_bikes:
            if garage.full():
                raise TypeError("This garage is full")
            else:
                garage.bikes.append(bike)
                self.bikes.remove(bike)
    
    def collect_working(self, garage):
        collect = [bike for bike in garage.bikes if bike.working]

        for working_bike in collect:
            if self.full():
                raise TypeError("This repairman can't take any more!")
            else:
                self.bikes.append(working_bike)
                garage.bikes.remove(working_bike)

    def deliver_working(self, docking_station):
        working_bikes = [bike for bike in self.bikes if bike.working]
        
        for bike in working_bikes:
            if docking_station.full():
                raise TypeError("This station is full")
            else:
                docking_station.bikes.append(bike)
                self.bikes.remove(bike)
    
    def full(self):
        return(len(self.bikes) >= self.capacity)


