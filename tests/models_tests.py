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

    @attr('maleathlete')
    def testWalkReducesEnergyLevel(self):
        athlete = models.MaleAthlete(1000)

        athlete.walk()
        self.assertEqual(athlete.energy_level, 999)

    @attr('maleathlete')
    def testWalkWithTimeUnitsReducesEnergyLevel(self):
        athlete = models.MaleAthlete(1000)

        athlete.walk(time=5)
        self.assertEqual(athlete.energy_level, 995)

    @attr('maleathlete')
    def testJogReducesEnergyLevel(self):
        orig = 1000
        athlete = models.MaleAthlete(orig)

        athlete.jog()
        self.assertEqual(athlete.energy_level, orig-models.JOG_ENERGY)

    @attr('maleathlete')
    def testJogWithTimeUnitsReducesEnergyLevel(self):
        orig = 1000
        athlete = models.MaleAthlete(orig)

        athlete.jog(time=5)
        self.assertEqual(athlete.energy_level, orig-5*models.JOG_ENERGY)






if __name__ == "__main__":
    unittest.main()
