from models.constants import Symbols, Exceptions, Outputs

class Player:
    def __init__(self) -> None:
        self.name : str = None
        self.symbol : str  = None
        self.moves : list = []
        self.tries : int = 0
        self.max_tries : int = 5
    
    def get_player_name(self, player2 : bool = False) -> str:
        self.name = None
        self.tries = 0
        while (not self.name or not self.name.isalnum()) and self.tries < 5:
            try:
                self.tries += 1
                if player2:
                    self.name = input("Enter name for the player (Default Second player : Computer): ")
                else:
                    self.name = input("Enter name for the player : ")
                if not self.name and player2:
                    self.name = "Computer"
                    break
                elif not self.name or not self.name.isalnum():
                    raise NameError()
                elif self.name.lower() == "computer" and not player2:
                    raise ValueError()
                else:
                    break
            except NameError:
                print(f"{Exceptions.INVALID_VALUE_FOR_NAME.value}")
                print(f"{self.max_tries - self.tries} attempt(s) left.")
            except ValueError:
                print(f"{Exceptions.INVALID_VALUE_FOR_FIRST_NAME.value}")
                print(f"{self.max_tries - self.tries} attempt(s) left.")
            except:
                print(f"{Exceptions.INVALID_INPUT} Try again..")
                print(f"{self.max_tries - self.tries} attempt(s) left.")
        if not self.name or not self.name.isalnum():
            print("Attempts exhausted.")
            return Exceptions.INVALID_VALUE_FOR_NAME.value
        return Outputs.VALID_NAME.value

    def get_player_symbol(self) -> str:
        """ This funciton provides and assigns the symbol for the First player based on his choice. The symbol for the Second player will be assigned automatically."""
        self.symbol = input(f"Enter your choice of symbol :\n1.{Symbols.X.value}(Default)\n2.{Symbols.O.value}\n")
        if not self.symbol == "2":
            self.symbol = Symbols.X.value
        else:
            self.symbol = Symbols.O.value
        return Outputs.VALID_SYMBOL.value
        
    def __str__(self) -> any:
        return print(f"The player's name is {self.name} and symbol is {self.symbol}.")
