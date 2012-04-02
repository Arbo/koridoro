#coding: utf-8

WALK_ENERGY = 1
JOG_ENERGY = 5

class MaleAthlete(object):
    def __init__(self, energy_level=None):
        self.energy_level = energy_level

    def walk(self, time=1):
        self.energy_level -= WALK_ENERGY*time

    def jog(self, time=1):
        self.energy_level -= JOG_ENERGY*time
