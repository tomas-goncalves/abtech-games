import random

SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        [
         '.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O.',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ],
]

WIDTH, HEIGHT = 7, 18

board = [[0] * WIDTH for _ in range(HEIGHT)]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = 0

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0  # Add score attribute

    def new_piece(self):
            # Choose a random shape
            shape = random.choice(SHAPES)
            # Return a new Tetromino object
            return Tetromino(self.width // 2, 0, shape)

    def valid_move(self, piece, x, y, rotation):
        """Check if the piece can move to the given position"""
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
            for j, cell in enumerate(row):
                # Calculate the new position
                new_x = piece.x + j + x
                new_y = piece.y + i + y

                # Check if the cell is out of bounds on the left
                if cell == 'O' and (new_x < 0 or new_y < 0 or new_y >= len(self.grid) or new_x >= len(self.grid[0])):
                    return False

                # Check if the cell overlaps with an existing cell in the grid
                if cell == 'O' and self.grid[new_y][new_x] != 0:
                    return False

        return True

    def clear_lines(self):
        """Clear the lines that are full and return the number of cleared lines"""
        lines_cleared = 0
        for i, row in enumerate(self.grid[:-1]):
            if all(cell != 0 for cell in row):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])
        return lines_cleared

    def lock_piece(self, piece):
        """Lock the piece in place and create a new piece"""
        for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.grid[piece.y + i][piece.x + j] = 255
        # Clear the lines and update the score
        lines_cleared = self.clear_lines()
        self.score += lines_cleared * 100  # Update the score based on the number of cleared lines
        # Create a new piece
        self.current_piece = self.new_piece()
        # Check if the game is over
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True
        return lines_cleared

    def update(self):
        """Move the tetromino down one cell"""
        print("Running")
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                print("moving piece down")
                self.current_piece.y += 1
            else:
                print("piece at the end")
                self.lock_piece(self.current_piece)

    # Returns a 2d array of brightness values
    def draw(self):
        """Draw the grid and the current piece"""
        board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    board[y][x] = 127

        if self.current_piece:
            for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':

                        board[self.current_piece.y + i][self.current_piece.x + j] = 255
        return board

game = None

fall_time = 0
fall_speed = 160
held_time = -1
last_input = None

def init():
    global game
    game = Tetris(WIDTH, HEIGHT)

def update(input, delta_time):
    global fall_time, fall_speed, held_time, last_input
    global game
    if not game:
        print("NO GAME")
        return
    if input:
        go = True
        if held_time == -1:
            held_time = 0
        if input == last_input:
            held_time += delta_time
            if held_time < 100:
                go = False
            else:
                held_time = 0

        last_input = input

        if go:
            if input ==  "a":
                if game.valid_move(game.current_piece, -1, 0, 0):
                    game.current_piece.x -= 1 # Move the piece to the left
            if input == "d":
                if game.valid_move(game.current_piece, 1, 0, 0):
                    game.current_piece.x += 1 # Move the piece to the right
            if input == "s":
                if game.valid_move(game.current_piece, 0, 1, 0):
                    game.current_piece.y += 1 # Move the piece down
            if input == "w":
                if game.valid_move(game.current_piece, 0, 0, 1):
                    game.current_piece.rotation += 1 # Rotate the piece
            # if event.key == pygame.K_SPACE:
            #     while game.valid_move(game.current_piece, 0, 1, 0):
            #         game.current_piece.y += 1 # Move the piece down until it hits the bottom
            #     game.lock_piece(game.current_piece) # Lock the piece in place
    if not input:
        last_input = None
        held_time = -1
    # Get the number of milliseconds since the last frame
    fall_time += delta_time
    if fall_time >= fall_speed:
        # Move the piece down
        game.update()
        # Reset the fall time
        fall_time = 0

    data = game.draw()

    if game.game_over:
        # Draw the "Game Over" message
        # draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message
        # You can add a "Press any key to restart" message here
        # Check for the KEYDOWN event
        if input:
            # Create a new Tetris object
            game = Tetris(WIDTH, HEIGHT)

    return data
