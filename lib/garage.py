from lib.bike_methods import BikeMethods

class Garage(BikeMethods):
    def repair(self, bike):
        if bike.working:
            raise NotImplementedError("This bike already works.")
        else:
            bike.working = True