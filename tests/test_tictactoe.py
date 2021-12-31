from unittest import TestCase, mock
from unittest.case import expectedFailure
from models.players import Player
from tictactoe import TicTacToe
from models.constants import Outputs, Exceptions
from models.players import Player

class TestTicTacToe(TestCase):
    def test_show_rules(self):
        for _ in range(6):
            game = TicTacToe()
            result = game.show_rules()
            self.assertEqual(result, Outputs.RULES_DISPLAYED.value)

    @mock.patch('models.players.Player.get_player_name')
    @mock.patch('models.players.Player.get_player_symbol')
    @mock.patch('models.players.Player.get_player_name')
    def test_get_players_details_errors(self, p1_names, p1_symbols, p2_names):
        sample_p1_names = [Outputs.VALID_NAME.value, Outputs.VALID_NAME.value, Outputs.VALID_NAME.value, Outputs.VALID_NAME.value, Outputs.VALID_NAME.value]
        sample_p1_symbols = [Outputs.VALID_SYMBOL.value, Outputs.VALID_SYMBOL.value, Outputs.VALID_SYMBOL.value, Outputs.VALID_SYMBOL.value, Outputs.VALID_SYMBOL.value]
        for index in range(len(sample_p1_names)):
            p1_names.return_value = sample_p1_names[index]
            p1_symbols.return_value = sample_p1_symbols[index]
            p2_names.return_value = sample_p1_names[index]
            game = TicTacToe()
            result = game.get_players_details()
            self.assertEqual(result, Exceptions.INVALID_INPUT.value)
    
    @mock.patch('builtins.input') 
    def test_play(self, mock_input):
        slots = [
            ["1","2","3","6","4","8","5","7","9"],
            ["2","1","4","3","6","5","8","7","9"],
            ["1","2","3","6","4","7","5","9","8"],
            ["1","5","3","4","8","9","7","6","2"]
        ]
        expected_results = Outputs.GAME_COMPLETED.value
        expected_winners = ["p2","p1","p1","p1"]
        for pos, inputs in enumerate(slots):
            game = TicTacToe()
            game.player1, game.player2  = Player(), Player()
            game.player1.name, game.player2.name = "p1", "p2"
            game.player1.symbol, game.player2.symbol = "X", "O"
            result = game.play()
            for index in range(len(inputs)):
                mock_input.return_value = inputs[index]
            self.assertEqual(game.winner, expected_winners[pos])
            self.assertEqual(result, expected_results)