import sys
import os
import pytest
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pieces.cell import Cell


@pytest.fixture
def cell():
    return Cell(0, 0)


def test_add_neighbor(cell):
    cell.add_neighbor()
    assert cell.alive_neighbors == 1


def test_isAlive(cell):
    cell.state = 1
    print('wo')
    assert cell.isAlive() == True


def test_reset_neighbors(cell):
    cell.alive_neighbors = 1
    cell.reset_neighbors()
    assert cell.alive_neighbors == 0


def test_update(cell):
    rules = {'birth': 3, 'low': 2, 'high': 3}
    cell.alive_neighbors = 3
    assert cell.update(rules) == True


def test__str__(cell):
    cell.state = 1
    assert str(cell) == '1'
