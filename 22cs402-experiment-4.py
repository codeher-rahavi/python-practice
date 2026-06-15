class ChessGame:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.white_turn = True

    def print_board(self):
        print("  a b c d e f g h")
        print(" +----------------+")

        for i in range(8):
            print(8 - i, end="| ")
            print(' '.join(self.board[i]), end=" |")
            print(8 - i)

        print(" +----------------+")
        print("  a b c d e f g h")
        print()

    def get_pawn_moves(self, row, col):
        moves = []
        direction = -1 if self.board[row][col].isupper() else 1
        start_row = 6 if self.board[row][col].isupper() else 1

        if self.board[row + direction][col] == ' ':
            moves.append((row + direction, col))

        if row == start_row and self.board[row + 2 * direction][col] == ' ':
            moves.append((row + 2 * direction, col))

        return moves

    def get_piece_moves(self, row, col):
        piece = self.board[row][col].lower()

        if piece == 'p':
            return self.get_pawn_moves(row, col)

        return []

    def is_valid_move(self, row, col, new_row, new_col):
        if new_row < 0 or new_row >= 8 or new_col < 0 or new_col >= 8:
            return False

        piece_moves = self.get_piece_moves(row, col)

        return (new_row, new_col) in piece_moves

    def make_move(self, row, col, new_row, new_col):
        piece = self.board[row][col]
        self.board[row][col] = ' '
        self.board[new_row][new_col] = piece
        self.white_turn = not self.white_turn

    def play_game(self):
        while True:
            self.print_board()
            print("White's turn" if self.white_turn else "Black's turn")

            source = input("Enter source square (e.g., a2) or type exit: ")

            if source.lower() == "exit":
                print("Exiting game...")
                break

            destination = input("Enter destination square (e.g., a4) or type exit: ")

            if destination.lower() == "exit":
                break

            source_col = ord(source[0]) - ord('a')
            source_row = 8 - int(source[1])

            dest_col = ord(destination[0]) - ord('a')
            dest_row = 8 - int(destination[1])

            if self.is_valid_move(source_row, source_col, dest_row, dest_col):
                self.make_move(source_row, source_col, dest_row, dest_col)
            else:
                print("Invalid move. Try again.\n")


game = ChessGame()
game.play_game()