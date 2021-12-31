from unittest import mock
from unittest import TestCase
from models.players import Player
from models.constants import Outputs
import module_under_test


class TestGetPlayerName(TestCase):
    @mock.patch('module_under_test.input', create=True)
    def test_get_player_name(self, mocked_input):
        mocked_input.side_effect = ["q"]
        result = Player.get_player_name()
        self.assertEqual(result, {Outputs.VALID_NAME.value})
