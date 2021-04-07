class Shore:
    def __init__(self, chickens, wolves, bank):
        self.chickens = chickens
        self.wolves = wolves
        self.bank = bank
        if(bank == 0):
            self.boat = True
        else:
            self.boat = False

    def move_chicken(shore, number):
        if(shore.boat == True):
            shore.chickens -= number
            return True
        else:
            return False


    def move_wolf(shore, number):
        if(shore.boat == True):
            shore.wolves -= number
            return True
        else:
            return False

    def add_chicken(shore, number):
        if(shore.boat == False):
            shore.chickens += number
            return True
        else:
            return False

    def add_wolf(shore, number):
        if(shore.boat == False):
            shore.wolves += number
            return True
        else:
            return False

    def check_shore(shore):
        if(shore.chickens == 0):
            return True
        elif(shore.chickens < shore.wolves):
            print("You Lose" + str(shore.chickens) + ", " + str(shore.wolves))
            return False
        else:
            return True

    def print_shore(shore):
        return("chickens: " + str(shore.chickens) + ", Wolves: " + str(shore.wolves) + ", Boat: " + str(shore.boat))
