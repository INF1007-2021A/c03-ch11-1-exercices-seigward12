"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	def __init__(self, name, power, min_level) -> None:
		self.__name = name
		self.poer = power
		self.min_level = min_level

	UNARMED_POWER = 20

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls('unarmed', cls.UNARMED_POWER)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name : str, max_hp, attack, defence, level) -> None:
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defence = defence
		self.level = level
		self.hp = max_hp
		self.weapon = None

	@property
	def name(self):
		return self.__name

	def compute_damage(self, a, d):
		attaque = ((a.level*2/5 + 2) * a.weapon * (a.attack/d.defence))/50 + 2
		modifier = (random.randint(85, 100))/100 * (2 if random.randint(1,16)==16 else 1)
		retun attaque*modifier


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	damage = attacker.compute_damage(attacker, defender)
	
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
