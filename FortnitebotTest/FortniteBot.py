class FortniteBot: #class

    max_health = 100 #class attribute

    def __init__(self, bot_name, starting_health):     #constructor
        self.name = bot_name #attribute
        self.health = 100 #attribute

    def take_damage(self, amount): #method
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} is dead!")