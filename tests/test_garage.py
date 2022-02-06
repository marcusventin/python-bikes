# import unittest
# from unittest.mock import Mock

# from lib.garage import Garage

# class TestGarage(unittest.TestCase):
#     def test_accept_adds_bikes(self):
#         garage = Garage()

#         broken1 = Mock()
#         broken1.status = "released"
#         broken1.working = False

#         broken2 = Mock()
#         broken2.status = "released"
#         broken2.working = False

#         broken3 = Mock()
#         broken3.status = "released"
#         broken3.working = False

#         broken_bikes = [broken1, broken2, broken3]

#         garage.accept(broken_bikes)

#         self.assertIn(broken1, garage.bikes)
#         self.assertIn(broken2, garage.bikes)
#         self.assertIn(broken3, garage.bikes)
