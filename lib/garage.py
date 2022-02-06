import random

from lib.bike_mixin import BikeMixin

class Garage(BikeMixin):
    def repair(self, bike):
        confirmations = ["Clink!", "Screw!", "Bend!", "Inflate!",
            "Alter Saddle!"]
        if bike.working:
            raise NotImplementedError("This bike already works.")
        else:
            bike.working = True
            print(random.choice(confirmations))
