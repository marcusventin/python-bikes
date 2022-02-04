import unittest

from lib.docking_station import DockingStation
from lib.bike import Bike

class TestDockingStation(unittest.TestCase):
    def test_constructs(self):
        DockingStation()
    
    def test_release_bike(self):
        dock = DockingStation()
        bike = Bike("docked", "working")
        dock.bikes.append(bike)
        dock.release_bike(bike)
        
        self.assertEqual(bike.status, "released")
