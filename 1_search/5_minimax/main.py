import copy


class Cell:
    """Class to represent a single cell on the board."""

    def __init__(self, value=" "):
        self.value = value

    def is_empty(self):
        return self.value == " "

    def set_value(self, value: bool):
        if not self.is_empty():
            return False
        self.value = "X" if value else "O"
        return True

    def __str__(self):
        return self.value

    def __eq__(self, other: str):
        return self.value == other

    def __deepcopy__(self, memo):
        # Create a new Cell instance with copied attributes
        new_cell = Cell(self.value)
        return new_cell


class Board:
    """Class to manage the game board."""

    def __init__(self):
        self.board = [Cell() for i in range(9)]

    def display(self):
        print("\n-----------\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        for i in range(1, 3):  # Loop through 3 rows
            print("---+---+---")
            print(
                f" {self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]}"
            )
        print("\n-----------\n")

    def is_valid_cell(self, id):
        return id >= 0 and id <= 8 and self.board[id].is_empty()

    def make_move(self, position, symbol):
        if self.is_valid_cell(position):
            self.board[position] = symbol
            return True
        return False

    def is_full(self):
        for cell in self.board:
            if cell.is_empty():
                return False
        return True

    def fill(self, cell_id: int, value: bool):
        if not self.is_valid_cell(cell_id):
            return False

        self.board[cell_id].set_value(value)
        return True

    def check_winner(self):
        win_conditions = [
            # Rows
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            # Columns
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            # Diagonals
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in win_conditions:
            if self.board[a] != " " and (
                self.board[a] == self.board[b] == self.board[c]
            ):
                return True  # A winning sequence is found

        return False  # No winning sequence


class PlayerStrategy:
    """Abstract strategy for player moves."""

    def get_move(self):
        raise NotImplementedError("Subclasses should implement this method.")


class HumanPlayer(PlayerStrategy):
    """Strategy for a human player."""

    def __init__(self, name):
        self.name = name

    def get_move(self):
        while True:
            try:
                return int(input(f"{self.name}, enter your move (1-9): ")) - 1
            except ValueError:
                print("Please enter a valid number.")


class AIPlayer(PlayerStrategy):
    """Strategy for an AI player."""

    def __init__(self, name, board, is_maximizing=True):
        self.name = name
        self.board = board
        self.is_maximizing = is_maximizing

    def _get_eligible_move(self, board: Board):
        eligible_move = []
        for i in range(9):
            if board.is_valid_cell(i):
                eligible_move.append(i)
        return eligible_move

    def _max_value(self, current_board: Board):
        if current_board.check_winner():
            return (-1, None)

        if current_board.is_full():
            return (0, None)

        best_move = None
        best_score = float("-inf")

        for move in self._get_eligible_move(current_board):
            board = copy.deepcopy(current_board)
            board.fill(move, True)
            result = self._min_value(board)
            move_score = max(best_score, result[0])
            if move_score > best_score:
                best_score = move_score
                best_move = move
        return (best_score, best_move)

    def _min_value(self, current_board: Board):
        if current_board.check_winner():
            return (1, None)

        if current_board.is_full():
            return (0, None)

        best_move = None
        best_score = float("inf")

        for move in self._get_eligible_move(current_board):
            board = copy.deepcopy(current_board)
            board.fill(move, False)
            result = self._max_value(board)
            move_score = min(best_score, result[0])
            if move_score < best_score:
                best_score = move_score
                best_move = move
        return (best_score, best_move)

    def get_move(self):
        print(f"AI {self.name} is thinking...")
        start_board = copy.deepcopy(self.board)
        result = (
            self._max_value(start_board)
            if self.is_maximizing
            else self._min_value(start_board)
        )
        print(f"AI {self.name} has chosen: {result[1] + 1}")
        return result[1]


class TicTacToe:
    def __init__(self):
        print("Welcome to Tic Tac Toe!")
        self.board = Board()
        self.player1 = self._create_player(1)
        self.player2 = self._create_player(2)
        self.current_player = self.player1

    def _create_player(self, player_number):
        while True:
            choice = input(f"Is Player {player_number} an AI? (y/n): ").strip().lower()
            if choice == "y":
                return AIPlayer(
                    f"Player {player_number}", self.board, player_number == 1
                )
            elif choice == "n":
                return HumanPlayer(f"Player {player_number}")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def _switch_player(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play(self):
        print("Game Start!")
        self.board.display()

        while True:
            move = self.current_player.get_move()
            if self.board.fill(move, self.current_player == self.player1):
                self.board.display()

                winner = self.board.check_winner()
                if winner:
                    print(f"{self.current_player.name} wins!")
                    break
                elif self.board.is_full():
                    print("It's a draw!")
                    break

                self._switch_player()
            else:
                print("Invalid move. Try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
