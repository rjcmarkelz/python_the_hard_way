class LivingThing():
    def __init__(self, name, health, magicPoints, inventory):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.inventory = inventory
        self.hunger = 0

hero = LivingThing('Cody', 50, 80, {})
hero.hunger


monsters = [] #empty list
monsters.append(LivingThing('Goblin', 20, 0, {'gold': 12, 'dagger': 1}))
monsters.append(LivingThing('Dragon', 300, 200, {'gold':890, 'magic amulet': 1}))

