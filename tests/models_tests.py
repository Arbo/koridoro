#coding: utf-8

import mock
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
    @attr('maleathlete')
    def testJogWalksWhenNoEmergy(self):
        #Tests if the athelete has to walk if the energy_level is too low
        begin = models.JOG_ENERGY - 1

        athlete = models.MaleAthlete(begin)
        athlete.jog()

        self.assertTrue(athlete.walk.called)


        athlete.jog(time=5)
        self.assertEqual(athlete.energy_level, orig-5*models.JOG_ENERGY)

    @attr('maleathlete')
    def testJogWalksWhenNoEmergy(self):
        #Tests if the athelete has to walk if the energy_level is too low
        begin = models.JOG_ENERGY - 1

        athlete = models.MaleAthlete(begin)
        athlete.walk = mock.Mock()
        athlete.jog()

        self.assertTrue(athlete.walk.called)

    @attr('maleathlete')
    def testJogDoeOnlyReduceWalkLevelWhenNoEmergy(self):
        #Tests if the energy_level of the athelete is only reduced by the
        #walk action
        begin = models.JOG_ENERGY - 1

        athlete = models.MaleAthlete(begin)
        athlete.jog()

        self.assertEqual(athlete.energy_level, begin-models.WALK_ENERGY)






if __name__ == "__main__":
    unittest.main()
