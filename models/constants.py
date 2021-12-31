from enum import Enum


class Symbols(Enum):
    X = "X"
    O = "O"

class Greetings(Enum):
    WELCOME = "########################## WELCOME TO THE GAME : TIC TAC TOE ##########################"
    RULES = "########################## RULES OF THE GAME ##########################"
    PLAY_STARTED = "########################## STARTED NEW GAME ##########################"
    PLAY_COMPLETED = "########################## GAME COMPLETED ##########################"
    THANK_YOU = "########################## DO COME BACK FOR MORE ##########################"

class Details(Enum):
    RULES = """
    Minimum 1 player is required to play a game. If there is no 2nd player, Computer by default will become the 2nd player.
    There are 9 slots in a 3X3 format, available to be filled.
    The Player1 starts the game and each player will get the chance alternatively.
    These slots can be filled vertically, horizontally or diagonally and in any order.
    The game ends when:
        1. A player fills 3 consecutive slots with his Symbol, hence with a decisive result : Win/Lose.
        2. There are no more slots to be filled, hence a Draw.
    """
    MOVES = "Press available slots between 1-9 to fill the respective slots."

class Exceptions(Enum):
    INVALID_VALUE_FOR_NAME = "The name should consists of only characters and/or numerics."
    INVALID_VALUE_FOR_FIRST_NAME = "The First name should should not be Computer/computer."
    INVALID_INPUT = "The input is invalid."
    INVALID_SLOT = "Invalid slot, please choose from the available slots."
    SHOW_RULES_EXCEPTION = "Looks like your are looking for something which is not part of the rules. Hence, kindly refer documentation for more information. Exiting..."

class Outputs(Enum):
    VALID_NAME = "A valid name is set."
    VALID_SYMBOL = "A valid symbol is set."
    RULES_DISPLAYED = "Rules are shown."
    PLAYERS_DETAILS_SET = "Players' details are validated and set."
    GAME_COMPLETED = "The game is completed."
    GAME_CRASHED = "The game crashed, unexpectedly."

class Results(Enum):
    DECISIVE = "The game ended with a winner."
    DRAW ="The game ended as a draw."