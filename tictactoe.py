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
        self.single_player_game : bool = False

    def get_players_details(self) -> str:
        """ This function gets the player's details. """
        print(Greetings.PLAY_STARTED.value)
        self.player1 = Player()
        print("Give details for First player :\n")
        p1_name_returned = self.player1.get_player_name()
        if p1_name_returned == Exceptions.INVALID_VALUE_FOR_NAME.value:
            return Exceptions.INVALID_VALUE_FOR_NAME.value
        self.player1.get_player_symbol()
        print("Give details for Second player :\n")
        self.player2 = Player()
        self.player2.get_player_name(True)
        if self.player2.name == "Computer":
            self.single_player_game = True
        else:
            tries = 5
            while self.player1.name == self.player2.name and tries > 1:
                tries -= 1
                print(f"Player 1 : {self.player1.name}, cannot play also as Player2. {tries} attempt(s) left.")
                self.player2.get_player_name(True)
            if self.player1.name == self.player2.name or tries == 1:
                print("Attempts exhausted. Exiting...")
                return Exceptions.INVALID_INPUT.value
        self.player2.symbol = Symbols.X.value if self.player1.symbol == Symbols.O.value else Symbols.O.value
        return Outputs.PLAYERS_DETAILS_SET.value

    def show_rules(self) -> str:
        """ This function displays the rules of the self. """
        try:
            print(Greetings.RULES.value)
            print(Details.RULES.value)
            return Outputs.RULES_DISPLAYED.value
        except:
            return Exception

    def __choose_based_on_list(self, move_list):
        """ The __choose_based_on_list is a private function which will only be called from __choose_slot_for_computer function of the class. This function determines the slot to be shoosen for the computer based on the available details. """
        if len(move_list) > 1:
            if "5" in move_list:
                if "1" in move_list: return "9"
                if "2" in move_list: return "8"
                if "3" in move_list: return "7"
                if "6" in move_list: return "6"
                if "6" in move_list: return "4"
                if "7" in move_list: return "3"
                if "9" in move_list: return "2"
                if "9" in move_list: return "1"
            if "1" in move_list and "2" in move_list: return "3"
            if "1" in move_list and "3" in move_list: return "2"
            if "1" in move_list and "4" in move_list: return "7"
            if "1" in move_list and "7" in move_list: return "4"
            if "1" in move_list and "9" in move_list: return "5"

            if "2" in move_list and "3" in move_list: return "1"
            if "2" in move_list and "8" in move_list: return "5"

            if "3" in move_list and "6" in move_list: return "9"
            if "3" in move_list and "7" in move_list: return "5"
            if "3" in move_list and "9" in move_list: return "6"

            if "4" in move_list and "6" in move_list: return "5"
            if "4" in move_list and "7" in move_list: return "1"

            if "6" in move_list and "9" in move_list: return "3"

            if "7" in move_list and "8" in move_list: return "9"
            if "7" in move_list and "9" in move_list: return "8"

            if "8" in move_list and "9" in move_list: return "7"

        if not move_list:
            if self.board.grid[4] == None: return "5"
            if self.board.grid[0] == None: return "1"
            if self.board.grid[2] == None: return "3"
            if self.board.grid[6] == None: return "7"
            if self.board.grid[8] == None: return "9"
        
        return None

    def __choose_slot_for_computer(self):
        """ The __choose_slot_for_computer is a private function which will only be called from play function of the class. This function individually passes the move_list of the players to __choose_based_on_list to determines the slot to be shoosen for the computer based on the available details. """
        result = self.__choose_based_on_list(self.player2.moves)
        if result: return result
        result = self.__choose_based_on_list(self.player1.moves)
        if result: return result
        for i in range(1,10):
            if i not in self.player1.moves and i not in self.player2.moves:
                return i

    def play(self) -> str:
        """ This function starts and monitor's the ongoing self. """
        self.board = Board()
        while None in self.board.grid:
            self.input_tries = 0
            self.slot = None
            if self.player_ones_move:
                print(f"{self.player1.name}'s Turn. {Details.MOVES.value}")
            elif not self.player_ones_move and self.single_player_game:
                print(f"{self.player2.name}'s Turn.")
                self.slot = self.__choose_slot_for_computer()
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
                print(f"Attempts exhausted.\n")
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
    
    def __str__(self) -> any:
        return print(f"The current players are {self.player1.name} and {self.player2.name}.")

def main():
    """ This is the function which will get the inputs from the endusers and executes appropriate functions/instances. """
    print(Greetings.WELCOME.value)
    max_rules_shown = 0
    while True:
        try:
            choice = input("Choose option\n1.Rules\n2.Play(default)\n3.Exit\n")
            if choice == "3":
                print(Greetings.THANK_YOU.value)
                break
            game = TicTacToe()
            if choice == "1":
                max_rules_shown += 1
                if max_rules_shown == 5:
                    print("Looks like your are looking for something which is not part of the rules. Hence, kindly refer documentation for more information. Exiting...")
                    break
                show_rules_result = game.show_rules()
                if show_rules_result == Outputs.RULES_DISPLAYED.value: continue
                else: return show_rules_result
            get_players_details_result = game.get_players_details()
            if get_players_details_result == Outputs.PLAYERS_DETAILS_SET.value: pass
            elif get_players_details_result == Exceptions.INVALID_VALUE_FOR_NAME.value:
                print("Exiting...")
                continue
            else: return Outputs.GAME_COMPLETED.value
            play_result = game.play()
            if play_result == Outputs.GAME_COMPLETED.value: pass
            else:
                print(f"{play_result}") 
                return Outputs.GAME_CRASHED.value
        except Exception as e:
            print(f"Exception : {e}")


if __name__ == "__main__":
    """ This is the main module where the execution starts. """
    try:
        main()
    except:
        print(Outputs.GAME_CRASHED.value)

