from models.constants import Details, Exceptions, Greetings, Outputs, Symbols, Results
from models.board import Board
from models.players import Player

class TicTacToe: 
    def __init__(self) -> None:
        """ This function initialises the minimum required details for the game, when this class gets instantiated. """
        self.player1 : Player = None
        self.player2 : Player = None
        self.board : Board = None
        self.player_ones_move : bool = True
        self.total_moves_played : int = 0
        self.completed : bool = False
        self.max_tries : int = 3
        self.valid_slots : list = ["1","2","3","4","5","6","7","8","9"]
        self.input_tries : int = 0
        self.slot : int = None
        self.result : str = None
        self.winner : str = None

    def get_players_details(self) -> str:
        """ This function gets the player's details. """
        print(Greetings.PLAY_STARTED.value)
        self.player1 = Player()
        print("Give details for First player :\n")
        self.player1.get_player_name()
        self.player1.get_player_symbol()
        print("Give details for Second player :\n")
        self.player2 = Player()
        self.player2.get_player_name()
        tries = 5
        while self.player1.name == self.player2.name and tries > 0:
            tries -= 1
            print(f"Player 1 cannot play also as Player2. {tries} attempt(s) left.")
            self.player2.get_player_name()
        if self.player1.name == self.player2.name:
            print("Exhausted attempts. Exiting...")
            return Exceptions.INVALID_INPUT.value
        self.player2.symbol = Symbols.X.value if self.player1.symbol == Symbols.O.value else Symbols.O.value
        return Outputs.PLAYERS_DETAILS_SET.value

    def show_rules(self) -> str:
        """ This function displays the rules of the self. """
        print(Greetings.RULES.value)
        print(Details.RULES.value)
        return Outputs.RULES_DISPLAYED.value

    def play(self) -> str:
        """ This function starts and monitor's the ongoing self. """
        self.board = Board()
        while None in self.board.grid:
            self.input_tries = 0
            self.slot = None
            if self.player_ones_move:
                print(f"{self.player1.name}'s Turn. {Details.MOVES.value}")
            else:
                print(f"{self.player2.name}'s Turn. {Details.MOVES.value}")
            
            while self.input_tries < self.max_tries and (self.slot not in self.valid_slots or self.board.grid[int(self.slot)-1] != None):
                self.input_tries += 1
                try:
                    self.slot = input()
                    if not self.slot:
                        raise Exception()
                    elif self.slot not in self.valid_slots or self.board.grid[int(self.slot)-1] != None:
                        raise ValueError()
                    else:
                        break
                except ValueError:
                    print(f"{Exceptions.INVALID_SLOT.value}")
                    print(f"{self.max_tries - self.input_tries} attempt(s) left.")
                except:
                    print(f"{Exceptions.INVALID_INPUT.value}")
                    print(f"{self.max_tries - self.input_tries} attempt(s) left.")
            if self.input_tries >= 3 and (self.slot not in self.valid_slots or self.board.grid[int(self.slot)-1] != None):
                print(f"The available attempts are exhausted.\n")
                self.result = Results.DECISIVE.value
                if not self.player_ones_move:
                    self.winner = self.player1.name
                    print(f"########################## {self.player1.name} Wins!!!! ##########################\n")
                else:
                    self.winner = self.player2.name
                    print(f"########################## {self.player2.name} Wins!!!! ##########################\n")
                self.completed = True 
                break
            self.board.grid[int(self.slot)-1] = self.player1.symbol if self.player_ones_move else self.player2.symbol
            self.player1.moves.append(self.slot) if self.player_ones_move else self.player2.moves.append(self.slot)
            print(f"Board : \n{self.board}")
            self.total_moves_played += 1
            if self.total_moves_played > 4:
                winner_symbol = self.board.check_result()
                if winner_symbol != None:
                    self.result = Results.DECISIVE.value
                    if winner_symbol == self.player1.symbol:
                        self.winner = self.player1.name
                        print(f"########################## {self.player1.name} Wins!!!! ##########################\n")
                    else:
                        self.winner = self.player2.name
                        print(f"########################## {self.player2.name} Wins!!!! ##########################\n")
                    self.completed = True 
                    break
            self.player_ones_move = not self.player_ones_move
        if not self.completed:
            self.result = Results.DRAW.value
            print(f"Its a Draw\n")
            print(Greetings.PLAY_COMPLETED.value)
        return Outputs.GAME_COMPLETED.value

def main():
    """ This is the function which will get the inputs from the endusers and executes appropriate functions/instances. """
    print(Greetings.WELCOME.value)
    max_rules_shown = 0
    while True:
        choice = input("Choose option\n1.Rules\n2.Play(default)\n3.Exit\n")
        if choice == "3":
            print(Greetings.THANK_YOU.value)
            break
        game = TicTacToe()
        if choice == "1":
            max_rules_shown += 1
            if game.show_rules() == Outputs.RULES_DISPLAYED.value: pass
            continue
        if game.get_players_details() == Outputs.PLAYERS_DETAILS_SET.value: pass
        else: return Outputs.GAME_COMPLETED.value
        if game.play() == Outputs.GAME_COMPLETED.value: pass
        else: return Outputs.GAME_CRASHED.value


if __name__ == "__main__":
    """ This is the main module where the execution starts. """
    try:
        main()
    except:
        print(Outputs.GAME_CRASHED.value)

