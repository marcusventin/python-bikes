class Garage:
    def __init__(self):
        self.bikes = []

    def accept(self, broken_bikes):
        for bike in broken_bikes:
            self.bikes.append(bike)