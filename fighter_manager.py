#!/usr/bin/python
# -*- coding: utf-8 -*-

from fighter_game import Fighter, Weapon


class Fighter_manager:
    
    def __init__(self):
        self.fighter_list = []
        self.weapon_list = []

    def create_fighter(self):
        fighter = Fighter(str(input("Fighter name : ")), str(input("Description : ")))
        self.fighter_list.append(fighter)
        return fighter
        
        
    def create_weapon(self):
        weapon = Weapon(str(input("Weapon name : ")), input("Damage (be reasonable) : "), input("Number of ammo : "))
        self.weapon_list.append(weapon)
        return weapon
