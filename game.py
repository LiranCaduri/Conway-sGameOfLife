from os import system, name
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

    birth_rule = int(rules.get('birth'))
    first_revive = random.randint(birth_rule, 8)
    rand_pos = (random.randint(0, Board.number_of_columns - 1), random.randint(0, Board.number_of_columns - 1))

    keys = list(Board.direction_dict.keys())
    random.shuffle(keys)
    directions_shuffled = {key: Board.direction_dict[key] for key in keys }
    
    main_board.grid[rand_pos[0]][rand_pos[1]].state = 1 # middle
    for i, (x, y) in enumerate(directions_shuffled.values()):
        if i + 1 == first_revive:
            break
        else:
            if rand_pos[0] + x >= 0 and rand_pos[1] + y >= 0 and rand_pos[0] + x < 50 and rand_pos[1] + y < 50:
                main_board.grid[rand_pos[0] + x][rand_pos[1] + y].state = 1

    while True:
        print(main_board)
        sleep(0.4)
        clear()
        main_board.next_gen()

if __name__ == '__main__':
    rule = input('\nEnter the game rules like the next format: B<1-8>/S<1-8><1-8>.\nEvery other format will cause the program to go to the default: B3/S23\nYour input:\n')
    rules = re.match(r'B(?P<birth>[1-8])/S(?P<low>[1-8])(?P<high>[1-8])', rule)
    if rules is not None:
        game_of_life(rules.groupdict())
    else:
        clear()
        print("Running Default.....")
        sleep(1.5)
        clear()
    game_of_life()
