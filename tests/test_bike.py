import unittest

from lib.bike import Bike

class TestBike(unittest.TestCase):
    def test_constructs(self):
        Bike("docked", True)

    def test_release_sets_status_to_released(self):
        bike = Bike("docked", True)
        bike.release()
        self.assertEqual(bike.status, "released")
    
    def test_working(self):
        bike = Bike("docked", True)
        self.assertEqual(bike.working, True)
    
    def test_not_working(self):
        bike = Bike("docked", False)
        self.assertEqual(bike.working, False)
    
    def test_dock_changes_status(self):
        bike = Bike("released", True)
        bike.dock()

        self.assertEqual(bike.status, "docked")
    
    def test_report_changes_working_to_false(self):
        bike = Bike("released", True)
        bike.report()

        self.assertEqual(bike.working, False)