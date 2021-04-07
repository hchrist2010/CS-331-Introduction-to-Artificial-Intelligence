from Shore import Shore
class Game:
    def __init__(self, chickens, wolves):
        self.left = Shore(chickens, wolves, 0)
        self.right = Shore(0, 0, 1)
        self.chickens = chickens
        self.wolves = wolves

    def check_state(game):
        if(game.left.check_shore() and game.right.check_shore()):
            return True
        else:
            return False

    def check_goal(game):
        if(game.right.wolves == game.wolves and game.right.chickens == game.chickens):
            return True
        else:
            game.print_state()
            return False

    def move_left(game, animal, number):
        if(game.right.boat == False or number > 2):
            return False
        elif(animal == "chicken"):
            if(game.right.move_chicken(number) and game.left.add_chicken(number)):
                game.right.boat = False
                game.left.boat = True
                return game.check_state()
            else:
                return False
        elif(animal == "wolf"):
            if(game.right.move_wolf(number) and game.left.add_wolf(number)):
                game.right.boat = False
                game.left.boat = True
                return game.check_state()
            else:
                return False
        elif(animal == "both" and number == 2):
            if(game.right.move_wolf(1) and game.right.move_chicken(1) and game.left.add_wolf(1) and game.left.add_chicken(1)):
                game.right.boat = False
                game.left.boat = True
                return game.check_state()
        else:
            print("Error, invalid move input")

    def move_right(game, animal, number):
        if(game.left.boat == False or number > 2):
            return False
        elif(animal == "chicken"):
            if(game.left.move_chicken(number) and game.right.add_chicken(number)):
                game.left.boat = False
                game.right.boat = True
                return game.check_state()
            else:
                return False
        elif(animal == "wolf"):
            if(game.left.move_wolf(number) and game.right.add_wolf(number)):
                game.left.boat = False
                game.right.boat = True
                return game.check_state()
            else:
                return False
        elif(animal == "both" and number == 2):
            if(game.left.move_wolf(1) and game.left.move_chicken(1) and game.right.add_wolf(1) and game.right.add_chicken(1)):
                game.left.boat = False
                game.right.boat = True
                return game.check_state()
        else:
            print("Error, invalid move input")

    def print_state(game):
        print()
        print("Left Shore: " + game.left.print_shore())
        print("Right Shore: " + game.right.print_shore())
