import unittest
from unittest.mock import Mock


from lib.docking_station import DockingStation

class TestDockingStation(unittest.TestCase): 
    def test_allows_for_custom_capacity(self):
        dock = DockingStation(5)

        self.assertEqual(dock.capacity, 5)

    def test_release_bike_doesnt_release_broken_bikes(self):
        dock = DockingStation()

        working = Mock()
        working.status = "docked"
        working.working = True

        broken = Mock()
        broken.status = "docked"
        broken.working = False

        dock.bikes = [broken, working]
        dock.release_bike()

        self.assertEqual(dock.bikes, [broken])
    
    def test_release_only_releases_one_bike(self):
        dock = DockingStation()

        working1 = Mock()
        working1.status = "docked"
        working1.working = True
        
        working2 = Mock()
        working2.status = "docked"
        working2.working = True

        working3 = Mock()
        working3.status = "docked"
        working3.working = True

        dock.bikes = [working1, working2, working3]
        dock.release_bike()

        self.assertEqual(len(dock.bikes), 2)
    
    def test_release_bike_raises_error_when_no_working_bikes(self):
        dock = DockingStation()

        broken = Mock()
        broken.status = "docked"
        broken.working = False

        dock.bikes = [broken]

        self.assertRaises(IndexError, dock.release_bike)

    def test_dock_adds_bike_to_station(self):
        dock = DockingStation()
        
        bike = Mock()
        bike.status = "released"
        bike.working = True

        dock.dock(bike)

        self.assertEqual(len(dock.bikes), 1)
        self.assertIn(bike, dock.bikes)

    def test_dock_raises_error_when_station_at_capacity(self):
        dock = DockingStation()
        
        bike = Mock()
        bike.status = "docked"
        bike.working = True
    
        dock.bikes = [bike for number in range(dock.capacity)]

        self.assertRaises(TypeError, dock.dock, bike)
    
    def test_dock_accepts_broken_bikes(self):
        dock = DockingStation()

        bike = Mock()
        bike.status = "released"
        bike.working = False

        dock.dock(bike)

        self.assertEqual(len(dock.bikes), 1)

    def test_full_returns_true_when_station_full(self):
        dock = DockingStation()

        bike = Mock()
        bike.status = "docked"
        bike.working = True

        dock.bikes = [bike for number in range(dock.capacity)]

        self.assertEqual(dock.full(), True)
    
    def test_full_returns_false_when_not_full(self):
        dock = DockingStation()

        self.assertEqual(dock.full(), False)
    
    def test_empty_returns_true_when_station_empty(self):
        dock = DockingStation()

        self.assertEqual(dock.empty(), True)

    def test_empty_returns_false_when_not_empty(self):
        dock = DockingStation()

        bike = Mock()
        bike.status = "docked"
        bike.working = False

        dock.bikes = [bike]

        self.assertEqual(dock.empty(), False)