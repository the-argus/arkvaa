"""This file describes the heroic adventurer Fester.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

from dungeonsheets.features.ranger import Archery

dungeonsheets_version = "0.18.0"

name = "Fester"
player_name = "Ian"

# Be sure to list Primary class first
classes = ['Ranger']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [2]  # ex: [10] or [3, 2]
subclasses = []  # ex: ['Necromacy'] or ['Thief', None]
background = "Outlander"
race = "Dark Elf"
alignment = "Chaotic neutral"

xp = 0
hp_max = 22
hp = 14
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 8
dexterity = 17
constitution = 13
intelligence = 10
wisdom = 14
charisma = 13

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('nature', 'insight', 'stealth', 'athletics', 'survival', 'perception')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Scimitar", "Longbow"]  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "Leather Armor"  # Eg "leather armor"
shield = "None"  # Eg "shield"

equipment = """
    
"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Infusions for Artificer
infusions = () # Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """Eccentric, Blunt, Socially Inept"""

ideals = """The lives of animals and plants are just as morally important as the lives of sentient humanoids"""

bonds = """Learn where he came from."""

flaws = """Sees sentient humanoids as actually less important plants and animals, despite his ideals."""

features_and_traits = """
    Favored Enemy: beasts
        You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.
    Favored Terrain: coast
        While traveling for an hour or more in your favored terrain, you gain the following benefits:

        Difficult terrain doesn’t slow your group’s travel.
        Your group can’t become lost except by magical means.
        Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.
        If you are traveling alone, you can move stealthily at a normal pace.
        When you forage, you find twice as much food as you normally would.
        While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.

    Fighting Style: Archery
        You gain a +2 bonus to attack rolls you make with ranged weapons.

    Spell save DC = 8 + your proficiency bonus + your Wisdom modifier
    Spell attack modifier = your proficiency bonus + your Wisdom modifier
"""
