import sys
import os
import pytest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pieces.board import Board


@pytest.fixture
def board():
    Board.number_of_rows = 4
    Board.number_of_columns = 4
    return Board(rules={'birth': 3, 'low': 2, 'high': 3})
    

def test_next_gen(board):
    board.grid[0][0].state = 1
    board.grid[1][1].state = 1
    board.grid[0][2].state = 1
    board.grid[2][0].state = 1
    board.grid[1][2].state = 1
    board.grid[2][2].state = 1

    new_gen = Board(board.rules)
    new_gen.grid[1][3].state = 1
    new_gen.grid[1][2].state = 1
    new_gen.grid[0][2].state = 1
    new_gen.grid[1][0].state = 1
    new_gen.grid[0][0].state = 1
    new_gen.grid[0][2].state = 1
    new_gen.grid[2][0].state = 1
    new_gen.grid[2][2].state = 1

    board.next_gen()
    assert str(board) == str(new_gen) and board.gen == 1
