import unittest
from unittest.mock import Mock

from lib.repair_man import RepairMan

class TestRepairMan(unittest.TestCase):
    def test_collect_broken_adds_broken_bikes_to_list(self):
        monty = RepairMan()

        broken1 = Mock()
        broken1.status = "docked"
        broken1.working = False

        working1 = Mock()
        working1.status = "docked"
        working1.working = True

        dock = Mock()
        dock.bikes = [working1, broken1]
        dock.capacity = 20

        monty.collect_broken(dock)

        self.assertEqual(len(monty.bikes), 1)
        self.assertIn(broken1, monty.bikes)
    
    def test_deliver_broken_removes_broken_bikes_from_list(self):
        monty = RepairMan()

        garage = Mock()
        garage.bikes = []

        broken1 = Mock()
        broken1.status = "released"
        broken1.working = False

        broken2 = Mock()
        broken2.status = "released"
        broken2.working = False

        working1 = Mock()
        working1.status = "released"
        working1.working = True

        monty.bikes = [broken1, working1, broken2]

        monty.deliver_broken(garage)

        self.assertIn(working1, monty.bikes)
        self.assertNotIn(broken1, monty.bikes)
        self.assertNotIn(broken2, monty.bikes)
    
    def test_collect_working_adds_working_to_list(self):
        monty = RepairMan()

        broken1 = Mock()
        broken1.status = "released"
        broken1.working = False

        broken2 = Mock()
        broken2.status = "released"
        broken2.working = False

        working1 = Mock()
        working1.status = "released"
        working1.working = True

        working2 = Mock()
        working2.status = "released"
        working2.working = True

        garage = Mock()
        garage.bikes = [broken1, working1, broken2, working2]

        monty.collect_working(garage)

        self.assertIn(working1, monty.bikes)
        self.assertIn(working2, monty.bikes)
        self.assertNotIn(broken1, monty.bikes)
        self.assertNotIn(broken2, monty.bikes)
    
    def test_deliver_working_removes_working_from_list(self):
        monty = RepairMan()

        broken1 = Mock()
        broken1.status = "released"
        broken1.working = False

        broken2 = Mock()
        broken2.status = "released"
        broken2.working = False

        working1 = Mock()
        working1.status = "released"
        working1.working = True

        working2 = Mock()
        working2.status = "released"
        working2.working = True

        monty.bikes = [broken1, working1, working2, broken2]

        dock = Mock()
        dock.bikes = []

        monty.deliver_working(dock)

        self.assertIn(broken1, monty.bikes)
        self.assertIn(broken2, monty.bikes)
        self.assertNotIn(working1, monty.bikes)
        self.assertNotIn(working2, monty.bikes)
