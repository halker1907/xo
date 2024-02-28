
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна и цвета
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

# Функция для отрисовки сетки
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), 5)
        pygame.draw.line(screen, WHITE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), 5)

# Функция для отрисовки крестиков и ноликов
def draw_XO(row, col, player):
    if player == 'X':
        pygame.draw.line(screen, WHITE, (col * WIDTH // 3, row * HEIGHT // 3), ((col + 1) * WIDTH // 3, (row + 1) * HEIGHT // 3), 5)
        pygame.draw.line(screen, WHITE, ((col + 1) * WIDTH // 3, row * HEIGHT // 3), (col * WIDTH // 3, (row + 1) * HEIGHT // 3), 5)
    else:
        pygame.draw.circle(screen, WHITE, ((col * WIDTH // 3) + WIDTH // 6, (row * HEIGHT // 3) + HEIGHT // 6), WIDTH // 6, 5)

# Создаем игровую доску
board = [['', '', ''], ['', '', ''], ['', '', '']]
turn = 'X'
game_over = False

def bot_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'
        draw_XO(row, col, 'O')
        return True
    return False
# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            row = y // (HEIGHT // 3)
            col = x // (WIDTH // 3)

            if board[row][col] == '':
                board[row][col] = turn
                draw_XO(row, col, turn)

                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                pygame.draw.line(screen, WHITE, (0, (i + 1) * HEIGHT // 3 - HEIGHT // 6), (WIDTH, (i + 1) * HEIGHT // 3 - HEIGHT // 6), 5)
                game_over = True
            if board[0][i] == board[1][i] == board[2][i] != '':
                pygame.draw.line(screen, WHITE, ((i + 1) * WIDTH // 3 - WIDTH // 6, 0), ((i + 1) * WIDTH // 3 - WIDTH // 6, HEIGHT), 5)
                game_over = True
        if board[0][0] == board[1][1] == board[2][2] != '':
            pygame.draw.line(screen, WHITE, (0, 0), (WIDTH, HEIGHT), 5)
            game_over = True
        if board[0][2] == board[1][1] == board[2][0] != '':
            pygame.draw.line(screen, WHITE, (WIDTH, 0), (0, HEIGHT), 5)
            game_over = True

        if all([cell != '' for row in board for cell in row]):
            game_over = True

        if game_over: #TODO закрывается раньше времени
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()


    draw_grid()

    pygame.display.flip()