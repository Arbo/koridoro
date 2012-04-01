#coding: utf-8

WALK_ENERGY = 1


class MaleAthlete(object):
    def __init__(self, energy_level=None):
        self.energy_level = energy_level

    def walk(self):
        self.energy_level -= WALK_ENERGY
