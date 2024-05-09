import pygame
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

# Function to draw grid lines
def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X
def draw_x(row, col):
    x = col * SQUARE_SIZE
    y = row * SQUARE_SIZE
    pygame.draw.line(screen, RED, (x + 10, y + 10), (x + SQUARE_SIZE - 10, y + SQUARE_SIZE - 10), 5)
    pygame.draw.line(screen, RED, (x + SQUARE_SIZE - 10, y + 10), (x + 10, y + SQUARE_SIZE - 10), 5)

# Function to draw O
def draw_o(row, col):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.circle(screen, BLUE, (x, y), SQUARE_SIZE // 2 - 10, 5)

# Function to check for winner
def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return True

    # Check columns
    for col in range(len(board[0])):
        check_col = [board[row][col] for row in range(len(board))]
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != 0:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        return True

    return False

# Function to check for draw
def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Main game loop
def main():
    board = [[0]*COLS for _ in range(ROWS)]
    player = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == 0:
                    if player == 1:
                        board[clicked_row][clicked_col] = 1
                        if check_winner(board):
                            print("Player 1 wins!")
                            game_over = True
                        elif check_draw(board):
                            print("Draw!")
                            game_over = True
                    else:
                        board[clicked_row][clicked_col] = 2
                        if check_winner(board):
                            print("Player 2 wins!")
                            game_over = True
                        elif check_draw(board):
                            print("Draw!")
                            game_over = True

                    player = player % 2 + 1

        screen.fill(WHITE)
        draw_grid()

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    draw_x(row, col)
                elif board[row][col] == 2:
                    draw_o(row, col)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
