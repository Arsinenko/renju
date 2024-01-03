import pygame
import time


def msg(text: str):
    # вывод сообщения на экран
    screen.fill(pygame.Color("black"))
    text = pygame.font.Font(None, 36).render(text, True, pygame.Color("white"))
    text_rect = text.get_rect(center=screen.get_rect().center)
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)


def clicked(x_pos: int, y_pos: int) -> list:
    # проверяет элемент массива по которому нажали
    for i in range(15):
        for j in range(15):
            if x_pos in range(i * cell_size + 2, i * cell_size + 2 + cell_size) and y_pos in range(j * cell_size + 2,
                                                                                                   j * cell_size + 2 + 35):
                board[i][j] = 'X' if first_player else "O"

                return [i, j]  # возвращаем элемент массива


def print_board():
    # выводим массив на экран
    for i in range(15):
        for j in range(15):
            if board[i][j] == '.':
                pygame.draw.rect(screen, black, (i * cell_size + 2, j * cell_size + 2, cell_size - 5, cell_size - 5))
            if board[i][j] == "X":
                screen.blit(X_image, (i * cell_size + 2, j * cell_size + 3))
            if board[i][j] == "O":
                screen.blit(O_image, (i * cell_size + 2, j * cell_size + 2))


def get_sign(board: list, x: int, y: int) -> str:
    # проверка на выход за приделы массива
    if x > 14 or y > 14 or x < 0 or y < 0:
        return '.'
    return board[x][y]


def win_line(line: list) -> bool:
    # проверяет победную комбинацию
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

RES = 600  # разрешение экрана
cell_size = 39  # размер клетки
screen = pygame.display.set_mode((RES, RES))

pygame.display.set_caption("GUI")
icon = pygame.transform.scale(pygame.image.load("images/icon.png"), (50, 50))  # иконка для приложения
pygame.display.set_icon(icon)
board = [['.' for _ in range(15)] for _ in range(15)]  # формирование игрового поля в виде массива
black = pygame.Color("black")

# избражение крестика
X_image = pygame.transform.scale(pygame.image.load("images/X_image.png"), (cell_size - 7, cell_size - 7))
# изображение нолика
O_image = pygame.transform.scale(pygame.image.load("images/O_images.png"), (cell_size - 7, cell_size - 7))

game_over = False
first_player = True  # определение игрока
while not game_over:
    # основной цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # проверка закрытия приложения
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos  # координаты клика мыши
            button = event.button  # назначение кнопки
            x = clicked(x_pos, y_pos)[0]
            y = clicked(x_pos, y_pos)[1]
            # линии в которых могут быть выигрышные комбинации
            vertical = [get_sign(board, x + i, y) for i in range(-4, 5)]
            horizontal = [get_sign(board, x, y + i) for i in range(-4, 5)]
            diagonal = [get_sign(board, x + i, y + i) for i in range(-4, 5)]
            diagonal2 = [get_sign(board, x + i, y - i) for i in range(-4, 5)]
            # проверка на победу
            if win_line(vertical) or win_line(horizontal) or win_line(diagonal) or win_line(diagonal2):
                msg("Game over!!!")
                time.sleep(5)
                game_over = True
            first_player = not first_player

    screen.fill(pygame.Color("white"))
    print_board()
    pygame.display.update()
