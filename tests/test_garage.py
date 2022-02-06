import unittest
from unittest.mock import Mock

from lib.garage import Garage

class TestGarage(unittest.TestCase):
    def test_repair_raises_error_if_bike_working(self):
        garage = Garage()
        
        working = Mock()
        working.status = "released"
        working.working = True

        self.assertRaises(NotImplementedError, garage.repair, working)
