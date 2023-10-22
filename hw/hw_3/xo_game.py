class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [[" " for _ in range(size)] for _ in range(size)]

    def draw(self):
        for row in self.cells:
            print("|".join(row))
        print("\n" + "-" * (self.size * 2 - 1))


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board, row, col):
        if board.cells[row][col] == " ":
            board.cells[row][col] = self.symbol
            return True
        else:
            return False


class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.player1 = Player("Игрок 1", "X")
        self.player2 = Player("Игрок 2", "O")

    def play(self):
        current_player = self.player1

        while True:
            self.board.draw()

            row = int(input(f"{current_player.name}, введите номер строки: ")) - 1
            col = int(input(f"{current_player.name}, введите номер столбца: ")) - 1

            if current_player.make_move(self.board, row, col):
                if self.check_win(current_player.symbol):
                    self.board.draw()
                    print(f"{current_player.name} победил!")
                    break

                if self.check_draw():
                    self.board.draw()
                    print("Ничья!")
                    break

                current_player = self.player2 if current_player == self.player1 else self.player1
            else:
                print("Недопустимый ход, попробуйте еще раз.")

    def check_win(self, symbol):
        for i in range(self.board.size):
            # Проверка по горизонтали
            if all(cell == symbol for cell in self.board.cells[i]):
                return True

            # Проверка по вертикали
            if all(row[i] == symbol for row in self.board.cells):
                return True

        # Проверка по диагоналям
        if all(self.board.cells[i][i] == symbol for i in range(self.board.size)):
            return True

        if all(self.board.cells[i][self.board.size - i - 1] == symbol for i in range(self.board.size)):
            return True

        return False

    def check_draw(self):
        return all(cell != " " for row in self.board.cells for cell in row)


if __name__ == "__main__":
    game = Game(3)
    game.play()