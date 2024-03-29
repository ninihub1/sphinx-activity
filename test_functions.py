import pytest
from tic_tac_bug_toe import is_win

class TestTicTacToe:

    def test_win(self):
        tictactoe_board = [['O', ' ', 'X'],
                           ['X', 'O', 'X'],
                           ['O', 'X', 'O']]
        assert is_win('O', tictactoe_board) == True