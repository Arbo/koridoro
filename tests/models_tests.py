#coding: utf-8

import unittest
from nose.plugins.attrib import attr

import koridoro.models as models


class MaleAtheleteTests(unittest.TestCase):
    @attr('maleathlete')
    def testInitenergy_level(self):
        energy_level = 100
        athlete = models.MaleAthlete(energy_level=energy_level)

        self.assertEqual(athlete.energy_level, energy_level)

    def testWalkReducesEnergyLevel(self):
        athlete = models.MaleAthlete(1000)

        athlete.walk()
        self.assertEqual(athlete.energy_level, 999)


if __name__ == "__main__":
    unittest.main()
