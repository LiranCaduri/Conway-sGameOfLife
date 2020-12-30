from os import system, name
from sys import argv
from time import sleep
import re
import   random

from pieces.board import Board

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def game_of_life(rules={'birth': 3, 'low': 2, 'high': 3}):
    main_board = Board(rules)

    birth_rule = rules.get('birth')
    rand_pos = (random.randint(0, Board.number_of_columns - 1),
                random.randint(0, Board.number_of_columns - 1))

    keys = list(Board.direction_dict.keys())
    random.shuffle(keys)
    directions_shuffled = {key: Board.direction_dict[key] for key in keys }
    
    for i, (x, y) in enumerate(directions_shuffled.values()):
        if i + 1 == birth_rule + 1:
            break
        else:
            main_board.grid[rand_pos[0] + x][rand_pos[1] + y].state = 1

    while True:
        print(main_board)
        sleep(0.65)
        clear()
        main_board.next_gen()

if __name__ == '__main__':
    if len(argv) >= 2: 
        rules = re.match(r'B(?P<birth>\d)/S(?P<low>\d)(?P<high>\d)', argv[1])
        # check if bigger then 8
        if rules is not None:
            game_of_life(rules.groupdict())
    else:
        game_of_life()
