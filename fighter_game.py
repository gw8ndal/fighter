#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange, uniform

class Fighter:
    """Base class of a fighter"""
    def __init__(self, name, description):
        self.__name = name #__=attribut privé
        self.__description = description
        self.__agility = randrange(1,9)
        self.__healthPoints = 100

    def get_name(self):
        """Return the name of the fighter"""
        return self.__name

    def get_description(self):
        """Return the description of the fighter"""
        return self.__description

    def set_description(self, description):
        """Set the description of the fighter"""
        self.__description = description

    def get_agility(self):
        """Return the agility of the fighter"""
        return self.__agility

    def get_strength(self):
        """Return the strength of the fighter"""
        return 10 - self.get_agility()

    def get_healthPoints(self):
        """Return the health of the fighter"""
        return self.__healthPoints

    def punch(self, a_fighter):
        """
        Punch a Fighter
        return the health points of a Fighter
        """
        points = int(uniform(0.7,1.0)*10*self.get_strength()/a_fighter.get_agility())
        a_fighter.__healthPoints =   a_fighter.get_healthPoints() - points
        return a_fighter.__healthPoints

    def summary(self):
        """Return the summary of a fighter"""
        name = 'name : ' + self.get_name()
        description = 'description : ' + self.get_description()
        agility = 'agility : ' + str(self.get_agility())
        strength = 'strength : ' + str(self.get_strength())
        healthPoints = 'healthPoints : ' + str(self.get_healthPoints())
        summary = '\n'.join([name, description, agility, strength, healthPoints])
        # if self.get_weapon():
            # summary += self.get_weapon().summary()
        return summary
