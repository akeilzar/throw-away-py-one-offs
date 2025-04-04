import curses
import random
import time

# Constants
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
TETROMINOES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
stdscr.nodelay(1)
stdscr.timeout(300)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(BOARD_HEIGHT, BOARD_WIDTH*2, 0, sw//2 - BOARD_WIDTH)

def draw_board(board):
    w.clear()
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x]:
                w.addch(y, x*2, '#')
    w.border()
    w.refresh()

def rotate(tetromino):
    return [list(row) for row in zip(*tetromino[::-1])]

def check_collision(board, tetromino, offset):
    off_x, off_y = offset
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell and (y + off_y >= BOARD_HEIGHT or
                         x + off_x >= BOARD_WIDTH or
                         x + off_x < 0 or
                         board[y + off_y][x + off_x]):
                return True
    return False

def merge_tetromino(board, tetromino, offset):
    off_x, off_y = offset
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = cell
    return board

def remove_full_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_removed = BOARD_HEIGHT - len(new_board)
    new_board = [[0]*BOARD_WIDTH for _ in range(lines_removed)] + new_board
    return new_board, lines_removed

def main(stdscr):
    board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    current_tetromino = random.choice(TETROMINOES)
    current_pos = [BOARD_WIDTH // 2 - len(current_tetromino[0]) // 2, 0]
    score = 0

    while True:
        draw_board(board)
        for y, row in enumerate(current_tetromino):
            for x, cell in enumerate(row):
                if cell:
                    w.addch(current_pos[1] + y, (current_pos[0] + x)*2, '#')
        w.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP:
            new_tetromino = rotate(current_tetromino)
            if not check_collision(board, new_tetromino, current_pos):
                current_tetromino = new_tetromino
        elif key == curses.KEY_DOWN:
            current_pos[1] += 1
            if check_collision(board, current_tetromino, current_pos):
                current_pos[1] -= 1
                board = merge_tetromino(board, current_tetromino, current_pos)
                board, lines_removed = remove_full_lines(board)
                score += lines_removed
                current_tetromino = random.choice(TETROMINOES)
                current_pos = [BOARD_WIDTH // 2 - len(current_tetromino[0]) // 2, 0]
                if check_collision(board, current_tetromino, current_pos):
                    break
        elif key == curses.KEY_LEFT:
            current_pos[0] -= 1
            if check_collision(board, current_tetromino, current_pos):
                current_pos[0] += 1
        elif key == curses.KEY_RIGHT:
            current_pos[0] += 1
            if check_collision(board, current_tetromino, current_pos):
                current_pos[0] -= 1
        else:
            current_pos[1] += 1
            if check_collision(board, current_tetromino, current_pos):
                current_pos[1] -= 1
                board = merge_tetromino(board, current_tetromino, current_pos)
                board, lines_removed = remove_full_lines(board)
                score += lines_removed
                current_tetromino = random.choice(TETROMINOES)
                current_pos = [BOARD_WIDTH // 2 - len(current_tetromino[0]) // 2, 0]
                if check_collision(board, current_tetromino, current_pos):
                    break

        draw_board(board)
        time.sleep(0.1)

    stdscr.nodelay(0)
    stdscr.addstr(sh//2, sw//2 - len("Game Over")//2, "Game Over")
    stdscr.addstr(sh//2 + 1, sw//2 - len(f"Score: {score}")//2, f"Score: {score}"






