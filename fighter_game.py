#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange

class Fighter:
    """Base class of a fighter"""
    def __init__(self, name, description):
        self.__name = name #__=attribut privé
        self.__description = description
        self.__agility = randrange(1,9)

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
