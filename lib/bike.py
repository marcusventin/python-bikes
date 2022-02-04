
class Bike:
    def __init__(self, status, working):
        self.status, self.working = status, working
    
    def release(self):
        self.status = "released"