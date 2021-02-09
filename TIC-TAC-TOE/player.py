import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass #lets you create an empty class without an error

class RandomComputerPlayer(Player): # child of Player
    def __init__(self, letter): # this init overrides the parent init
        super().__init__(letter) # super will make the child class inherit the methods and properties from the parent

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass