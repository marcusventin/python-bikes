import unittest

from lib.docking_station import DockingStation
from lib.bike import Bike

class TestDockingStation(unittest.TestCase):
    def test_constructs(self):
        DockingStation()
    
    def test_release_bike(self):
        dock = DockingStation()
        bike = Bike("docked", True)
        dock.bikes = [bike]
        dock.release_bike()

        self.assertEqual(bike.status, "released")
    
    def test_doesnt_release_broken_bike(self):
        dock = DockingStation()
        working = Bike("docked", True)
        broken = Bike("docked", False)
        dock.bikes = [broken, working]
        dock.release_bike()

        self.assertEqual(dock.bikes, [broken])
    
    def test_only_releases_one_bike(self):
        dock = DockingStation()
        working1 = Bike("docked", True)
        working2 = Bike("docked", True)
        working3 = Bike("docked", True)
        dock.bikes = [working1, working2, working3]
        dock.release_bike()

        self.assertEqual(len(dock.bikes), 2)
    
    def test_release_raises_error_when_station_is_empty(self):
        dock = DockingStation()

        self.assertRaises(IndexError, dock.release_bike)
    
    def test_dock_adds_bike_to_station(self):
        dock = DockingStation()
        bike = Bike("released", True)
        dock.dock(bike)

        self.assertEqual(len(dock.bikes), 1)

    def test_dock_raises_error_when_station_at_capacity(self):
        dock = DockingStation()
        bike = Bike("released", True)
        dock.bikes = [f"bike{number}" for number in range(dock.capacity)]
        
        self.assertRaises(TypeError, dock.dock, bike)

    def test_returns_true_when_station_full(self):
        dock = DockingStation()
        dock.bikes = [f"bike{number}" for number in range(dock.capacity)]

        self.assertEqual(dock.full(), True)
    
    def test_returns_false_when_not_full(self):
        dock = DockingStation()

        self.assertEqual(dock.full(), False)
    
    def test_returns_true_when_station_empty(self):
        dock = DockingStation()

        self.assertEqual(dock.empty(), True)

    def test_returns_false_when_not_empty(self):
        dock = DockingStation()
        dock.bikes = ["bike0"]

        self.assertEqual(dock.empty(), False)
    
    def test_allows_for_custom_capacity(self):
        dock = DockingStation(5)

        self.assertEqual(dock.capacity, 5)
