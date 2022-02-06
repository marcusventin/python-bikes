class Garage:
    def __init__(self):
        self.bikes = []

    def accept(self, broken_bikes):
        for bike in broken_bikes:
            self.bikes.append(bike)

    def despatch_working(self):
        working_bikes = [bike for bike in self.bikes if bike.working]

        while working_bikes:
            self.bikes.remove(working_bikes.pop())