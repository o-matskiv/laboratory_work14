from clboard import *


def main():
    print('Hewwo mai frend tudei wi r goin tu plai tic tac!\nPrezz entr to continiu')
    entr = input()
    board = Board()
    while not board.has_winner():
        print('Type your move')
        coor1 = int(input('>'))
        coor2 = int(input('>'))
        cell = (coor1, coor2)
        board.make_move(cell)
        print(board)
        print('------')
        print('Computer makes its move')
        board.make_random_move()
        print(board)
        print('------')


main()
