import unittest
from unittest.mock import Mock

from lib.repair_man import RepairMan

class TestRepairMan(unittest.TestCase):
    def test_collect_adds_broken_bikes_to_list(self):
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