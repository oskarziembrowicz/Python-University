
class Move(object):
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign

class Player(object):
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
    def get_move(self):
        print(self.name, ", enter x and y coordinates: ")
        x, y = map(int, input().split())
        return Move(x, y, self.sign)

class Board(object):
    def __init__(self):
        self.board = [['_', '_', '_'] for i in range(3)]

    def __str__(self):
        return self.get_state()

    def get_state(self):
        state = ""
        for row in self.board:
            state += "".join(row) + "\n"
        return state

    def get_field(self, x, y):
        return self.board[x][y]

    def set_field(self, move):
        if not (move.x in {0, 1, 2}) or not (move.y in {0, 1, 2}):
            print("Incorrect coordinates")
            return False
        if self.get_field(move.x, move.y) != '_':
            print("Incorrect coordinates")
            return False
        self.board[move.x][move.y] = move.sign
        return True

class Game(object):
    def __init__(self):
        self.board = Board()
        self.winning_sign = None

    def play(self, player_one, player_two):
        players = (player_one, player_two)
        current_player = 0
        while not self.game_over():
            while not self.board.set_field(
                players[current_player].get_move()):
                pass
            current_player = (current_player + 1) % 2
            print(self.board)
        if self.winning_sign == None:
            print("Tie!")
        elif self.winning_sign == player_one.sign:
            print(player_one.name, " wins!")
        else:
            print(player_two.name, " wins!")

    def game_over(self):
        for row in range(3):
            if self.board.get_field(row, 0) == \
                    self.board.get_field(row, 1) == \
                    self.board.get_field(row, 2) and \
                    self.board.get_field(row, 0) != '_':
                self.winning_sign = self.board.get_field(row, 0)
                return True
        for col in range(3):
            if self.board.get_field(0, col) == \
                    self.board.get_field(1, col) == \
                    self.board.get_field(col, 2) and \
                    self.board.get_field(0, col) != '_':
                self.winning_sign = self.board.get_field(0, col)
                return True
        if self.board.get_field(0, 0) == \
                self.board.get_field(1, 1) == \
                self.board.get_field(2, 2) and \
                self.board.get_field(0, 0) != '_':
            self.winning_sign = self.board.get_field(0, 0)
            return True
        if self.board.get_field(2, 0) == \
                self.board.get_field(1, 1) == \
                self.board.get_field(0, 2) and \
                self.board.get_field(2, 0) != '_':
            self.winning_sign = self.board.get_field(2, 0)
            return True
        if not self.is_next_move_possible():
            return True
        return False

    def is_next_move_possible(self):
        return '_' in self.board.get_state()

player_1 = Player("John", "O")
player_2 = Player('Stacy', 'X')
game = Game()
game.play(player_1, player_2)