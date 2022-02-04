import unittest

from lib.bike import Bike

class TestBike(unittest.TestCase):
    def test_constructs(self):
        Bike("docked", "working")

    def test_release_sets_status_to_released(self):
        bike = Bike("docked", "working")
        bike.release()
        self.assertEqual(bike.status, "released")
    
