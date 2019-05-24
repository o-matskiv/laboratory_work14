from clboard import *


def main():
    print('Press entr to continue')
    entr = input()
    board = Board()
    while not board.game_over():
            print('Type your move')
            while True:
                try:
                    coor1 = int(input('>'))
                    coor2 = int(input('>'))
                    cell = (coor1, coor2)
                    board.make_move(cell)
                    break
                except OutOfRangeError:
                    print('Coordinates must be in range [0,2]')
                except NotEmptyError:
                    print('Cell is already filled')

            print(board)
            print('------')
            print('Computer makes its move')
            board.make_best_move()
            print(board)
            print('------')


main()
