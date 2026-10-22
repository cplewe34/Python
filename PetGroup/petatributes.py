class pet_stuff:



    def __init__(self, pet_name, type, hunger, happiness, bond):
        self.name = pet_name
        self.type = type
        self.hunger = hunger
        self.hapiness = happiness
        self.bond = bond

    def play(self, play_time, hapiness, bond):

        self.hapiness += play_time
        self.bond += (play_time) / 2



    
        