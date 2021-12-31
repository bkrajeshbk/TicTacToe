from unittest import mock
from unittest import TestCase
from models.players import Player
from models.constants import Outputs, Exceptions


class TestPlayer(TestCase):
    @mock.patch('builtins.input') 
    def test_get_player_name(self, mock_input):
        passable_names = ["q","q1", "11", "qiweyoroiqwkanldfskjncakslnkncalsk", "80174891975641571983913", "bksjad81ihr1398rhf1h928djdj"]
        for index in range(len(passable_names)):
            mock_input.return_value= passable_names[index]
            player = Player()
            result = player.get_player_name()
            self.assertEqual(result, Outputs.VALID_NAME.value)
            self.assertEqual(player.name, passable_names[index])

    @mock.patch('builtins.input') 
    def test_get_player_name_errors(self, mock_input):
        exception_names = ["%", "1%", "*&^^&%$", ""]
        for index in range(len(exception_names)):
            mock_input.return_value= exception_names[index]
            player = Player()
            result = player.get_player_name()
            self.assertEqual(result, Exceptions.INVALID_VALUE_FOR_NAME.value)
    
    @mock.patch('builtins.input') 
    def test_get_player_symbol(self, mock_input):
        symbols = ["q","q1", "11", "qiweyoroiqwkanldfskjncakslnkncalsk", "80174891975641571983913", "bksjad81ihr1398rhf1h928djdj","%", "1%", "*&^^&%$", "","1","2"]
        excepted_symbols = ["X","X","X","X","X","X","X","X","X","X","X","O"]
        for index in range(len(symbols)):
            mock_input.return_value= symbols[index]
            player = Player()
            result = player.get_player_symbol()
            self.assertEqual(result, Outputs.VALID_SYMBOL.value)
            self.assertEqual(player.symbol, excepted_symbols[index])
