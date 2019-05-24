import random
from btree import *


class OutOfRangeError(Exception):
    pass


class NotEmptyError(Exception):
    pass


class Board:
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    def __init__(self):
        self.cells = [[0]*3 for i in range(3)]
        self.last_move = Board.NOUGHT
        self.WINNING_COMBINATION = self.generate_wining_combination()
        self._computer_points = 0
        self._player_points = 0

    def make_move(self, cell):
        if cell[0] > 2 or cell[1] > 2:
            raise OutOfRangeError('Coordinates must be in range [0,2]')
        if self.cells[cell[0]][cell[1]] != 0:
            raise NotEmptyError('Cell is already filled')
        self.last_move = - self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        return True

    @staticmethod
    def generate_wining_combination():
        combinations = []
        for i in range(3):
            combination1 = []
            combination2 = []
            for j in range(3):
                combination1.append((i, j))
                combination2.append((i, j))
            combinations.append(combination1)
            combinations.append(combination2)
        combinations.append([(0, 0), (1, 1), (2, 2)])
        combinations.append([(0, 2), (1, 1), (2, 0)])
        return combinations

    def built_tree(self):
        pass
        if self.game_over():
            return
        tree = LinkedBinaryTree(self.cells)

    def count_points(self, number):
        if number == 1:
            self._computer_points += 1
            print('I won, hahahaha')

        elif number == -1:
            self._player_points += 1
            print('Congratulations!!!!')
        elif number == 0:
            print("Oh, that's a draw!")
        print('Your points:{}. My  points:{}'.format(
            self._player_points, self._computer_points))
        return 0

    def game_over(self):
        for combination in self.WINNING_COMBINATION:
            lst = []
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])

            if max(lst) == min(lst) and max(lst) != 0:
                self.count_points(max(lst))
                return max(lst)
        possible_moves = self.find_possible_moves()
        if possible_moves == []:
            self.count_points(0)
            return 2
        return 0

    def find_possible_moves(self):
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        return possible_moves

    def make_random_move(self):
        possible_moves = self.find_possible_moves()
        if possible_moves == []:
            return
        cell = random.choice(possible_moves)
        self.last_move = - self.last_move
        self.cells[cell[0]][cell[1]] = self.last_move

    def make_best_move(self):
        board2 = self.copy()
        tree = BTree(board2)
        possible_moves = board2.find_possible_moves()
        if len(possible_moves) == 1:
            self.make_move(possible_moves[0])
        turn1 = random.choice(possible_moves)
        tree.insert_left(turn1)
        possible_moves.remove(turn1)
        turn2 = random.choice(possible_moves)
        tree.insert_right(turn2)

        def recursion(board2, turn, tree):
            board2.make_move(turn)
            if board2.game_over() == 1:
                return 1
            if board2.game_over() == -1 or board2.game_over() == 2:
                return 0
            if board2.game_over() == 0:
                find_possible_moves = board2.find_possible_moves()
                if len(find_possible_moves) == 1:
                    return recursion(board2, find_possible_moves[0], tree)
                turn1 = random.choice(possible_moves)
                tree.insert_left(turn1)
                possible_moves.remove(turn1)
                turn2 = random.choice(possible_moves)
                tree.insert_right(turn2)
                return recursion(board2, turn1, tree.left_child) + recursion(board2, turn2, tree.right_child)

        if recursion(board2, turn1, tree.left_child) > recursion(board2, turn2, tree.right_child):
            self.make_move(turn1)
        else:
            self.make_move(turn2)

    def copy(self):
        board2 = Board()
        board2.cells = self.cells
        board2.last_move = self.last_move
        return board2

    def __str__(self):
        transform = {0: '_', 1: 'o', -1: 'x'}
        return '\n'.join([''.join(map(lambda x: transform[x], row)) for row in self.cells])


if __name__ == '__main__':
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
