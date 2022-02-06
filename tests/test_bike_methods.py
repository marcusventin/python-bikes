import unittest
from unittest.mock import Mock

from lib.bike_methods import BikeMethods

class TestBikeMethods(unittest.TestCase):
    def test_allows_for_custom_capacity(self):
        container = BikeMethods(5)

        self.assertEqual(container.capacity, 5)
    
    def test_add_adds_to_bikes(self):
        bike = Mock()
        bike.status = "released"
        bike.working = True

        container = BikeMethods()
        container.add(bike)

        self.assertEqual(len(container.bikes), 1)
        self.assertIn(bike, container.bikes)
    
    def test_dock_raises_error_when_station_at_capacity(self):
        bike = Mock()
        bike.status = "docked"
        bike.working = True

        container = BikeMethods()
        container.bikes = [bike for number in range(container.capacity)]

        self.assertRaises(TypeError, container.add, bike)
    
    def test_remove_removes_from_bikes(self):
        bike = Mock()
        bike.status = "docked"
        bike.working = True

        container = BikeMethods()
        container.bikes = [bike]
        container.remove(bike)

        self.assertEqual(len(container.bikes), 0)
        self.assertNotIn(bike, container.bikes)
    
    def test_full_returns_true_when_container_full(self):
        bike = Mock()
        bike.status = "docked"
        bike.working = True

        container = BikeMethods()
        container.bikes = [bike for number in range(container.capacity)]

        self.assertEqual(container.full(), True)

    def test_full_returns_false_when_not_full(self):
        container = BikeMethods()

        self.assertEqual(container.full(), False)

    def test_empty_returns_true_when_station_empty(self):
        container = BikeMethods()

        self.assertEqual(container.empty(), True)

    def test_empty_returns_false_when_not_empty(self):
        bike = Mock()
        bike.status = "docked"
        bike.working = False

        container = BikeMethods()
        container.bikes = [bike]

        self.assertEqual(container.empty(), False)
