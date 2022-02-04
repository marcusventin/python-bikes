import unittest

from lib.docking_station import DockingStation
from lib.bike import Bike

class TestDockingStation(unittest.TestCase):
    def test_constructs(self):
        DockingStation()
    
    def test_release_bike(self):
        dock = DockingStation()
        bike = Bike("docked", True)
        dock.bikes.append(bike)
        dock.release_bike()

        self.assertEqual(bike.status, "released")
    
    def test_wont_release_broken_bike(self):
        dock = DockingStation()
        working = Bike("docked", True)
        broken = Bike("docked", False)
        dock.bikes.append(broken)
        dock.bikes.append(working)
        dock.release_bike()

        self.assertEqual(dock.bikes, [broken])
    
    def test_only_releases_one_bike(self):
        dock = DockingStation()
        working1 = Bike("docked", True)
        working2 = Bike("docked", True)
        working3 = Bike("docked", True)
        dock.bikes.append(working1)
        dock.bikes.append(working2)
        dock.bikes.append(working3)
        dock.release_bike()

        self.assertEqual(len(dock.bikes), 2)


