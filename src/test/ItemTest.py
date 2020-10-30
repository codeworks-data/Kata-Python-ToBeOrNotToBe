import unittest

from main.Item import Item
from enums.Locations import Locations
from enums.Names import Names


class RingTest(unittest.TestCase):
    car_in_paris = Item(Locations.PARIS, Names.CAR)
    car_in_paris_duplicate = Item(Locations.PARIS, Names.CAR)
    bus_in_paris = Item(Locations.PARIS, Names.BUS)
    car_in_dublin = Item(Locations.DUBLIN, Names.CAR)

    def test_duplicate(self):
        self.assertTrue(self.car_in_paris == self.car_in_paris_duplicate)

    def test_no_duplicate_same_location(self):
        self.assertFalse(self.car_in_paris == self.bus_in_paris)

    def test_no_duplicate_same_name(self):
        self.assertFalse(self.car_in_paris == self.car_in_dublin)
