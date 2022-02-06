class Bike:
    def __init__(self, status = "released", working = True):
        self.status, self.working = status, working
    
    def release(self):
        self.status = "released"
    
    def dock(self):
        self.status = "docked"

    def report(self):
        self.working = False
    
    def repair(self):
        self.working = True
    