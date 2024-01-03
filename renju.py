import pygame


def clicked(x_pos:int, y_pos:int) -> list:
    for i in range(15):
        for j in range(15):
            if x_pos in range(i * cell_size + 2, i * cell_size + 2 + cell_size ) and y_pos in range(j * cell_size + 2, j * cell_size + 2 + 35):
                board[i][j] = 'X' if first_player else "O"

                return [i, j]


def print_board():
    for i in range(15):
        for j in range(15):
            if board[i][j] == '.':
                pygame.draw.rect(screen, black, (i * cell_size + 2, j * cell_size + 2, cell_size - 5, cell_size-5))
            if board[i][j] == "X":
                screen.blit(X_image, (i * cell_size + 2, j * cell_size + 3))
            if board[i][j] == "O":
                screen.blit(O_image, (i * cell_size + 2, j * cell_size + 2))


def get_sign(board: list, x:int, y:int):
    if x > 14 or y > 14 or x < 0 or y < 0:
        return '.'
    return board[x][y]


def win_line(line: list) ->bool:
    n = 4
    count_left = 0
    count_right = 0
    for i in range(1, 5):
        if line[n - i] == line[n]:
            count_left += 1
        else:
            break
    for i in range(1, 5):
        if line[4 + i] == line[4]:
            count_right += 1
        else:
            break
    return True if count_left + count_right >= 4 else False


pygame.init()

RES = 600
cell_size = 39
screen = pygame.display.set_mode((RES, RES))

pygame.display.set_caption("GUI")
icon = pygame.transform.scale(pygame.image.load("images/icon.png"), (50, 50))
pygame.display.set_icon(icon)
board = [['.' for _ in range(15)] for _ in range(15)]
black = pygame.Color("black")

X_image = pygame.transform.scale(pygame.image.load("images/X_image.png"), (cell_size - 7, cell_size - 7))
O_image = pygame.transform.scale(pygame.image.load("images/O_images.png"), (cell_size - 7, cell_size - 7))


game_over = False
first_player = True
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos
            button = event.button
            x = clicked(x_pos, y_pos)[0]
            y = clicked(x_pos, y_pos)[1]
            vertical = [get_sign(board, x + i, y) for i in range(-4, 5)]
            horizontal = [get_sign(board, x, y + i) for i in range(-4, 5)]
            diagonal = [get_sign(board, x + i, y + i) for i in range(-4, 5)]
            diagonal2 = [get_sign(board, x + i, y - i) for i in range(-4, 5)]

            if win_line(vertical) or win_line(horizontal) or win_line(diagonal) or win_line(diagonal2):
                game_over = True
            first_player = not first_player

    screen.fill(pygame.Color("white"))
    print_board()
    pygame.display.update()
