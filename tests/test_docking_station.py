import unittest
from unittest.mock import Mock

from lib.docking_station import DockingStation

class TestDockingStation(unittest.TestCase): 
    def test_release_bike_doesnt_release_broken_bikes(self):
        working = Mock()
        working.status = "docked"
        working.working = True

        broken = Mock()
        broken.status = "docked"
        broken.working = False

        dock = DockingStation()
        dock.bikes = [broken, working]
        dock.release_bike()

        self.assertEqual(dock.bikes, [broken])
    
    def test_release_only_releases_one_bike(self):
        working1 = Mock()
        working1.status = "docked"
        working1.working = True
        
        working2 = Mock()
        working2.status = "docked"
        working2.working = True

        working3 = Mock()
        working3.status = "docked"
        working3.working = True

        dock = DockingStation()
        dock.bikes = [working1, working2, working3]
        dock.release_bike()

        self.assertEqual(len(dock.bikes), 2)
    
    def test_release_bike_raises_error_when_no_working_bikes(self):
        broken = Mock()
        broken.status = "docked"
        broken.working = False

        dock = DockingStation()
        dock.bikes = [broken]

        self.assertRaises(IndexError, dock.release_bike)
    
    def test_dock_accepts_broken_bikes(self):
        bike = Mock()
        bike.status = "released"
        bike.working = False

        dock = DockingStation()
        dock.dock(bike)

        self.assertEqual(len(dock.bikes), 1)
    