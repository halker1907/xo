
import pygame
import sys
from tkinter import *
from tkinter import messagebox as mb
# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна и цвета
WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

img = pygame.image.load('i.png')
# Создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики", icontitle="pixels.png") 
pygame.display.set_icon(img)
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
sound1 = pygame.mixer.Sound('sound_2.ogg')
sound2 = pygame.mixer.Sound('sound_1.ogg')
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    

        if not game_over and event.type == pygame.MOUSEBUTTONUP:
            sound2.play()
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
        elif game_over and event.type == pygame.MOUSEBUTTONUP: #ивент на нажатие НЕТ
            x_1, y_1 = pygame.mouse.get_pos()
            x_2, y_2 = pygame.mouse.get_pos()
            if x_1 >= WIDTH // 2 + 100 and x_1 <= 550 and y_1 >= 400 and y_1 <= 500:
                sound1.play()
                pygame.time.wait(200)
                sys.exit()
            elif x_2 <= WIDTH // 2 - 150 and x_2 >= 60 and y_2 >= 400 and y_2 <= 500:
                sound1.play()
                pygame.time.wait(100)
                info = mb.showinfo("Инфо", "Данная функция пока не доступна, для начала новой игры, перезапустите программу.")
                sound1.play()

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
            

        if game_over == True:
            font = pygame.font.Font("dewberry-italic.ttf", 60) #сайт шрифтов: https://ffont.ru/fonts
            text = font.render("Игра окончена!", True, (0, 200, 0))
            place = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 135))


            text_2 = font.render("Начать новую игру?", True, (0, 200, 0))
            place_2 = text_2.get_rect(center=(WIDTH // 2, HEIGHT // 2 ))

            text_3 = font.render("ДА", True, (0, 200, 0))
            place_3 = text_3.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2  + 150))

            text_4 = font.render("НЕТ", True, (0, 200, 0))
            place_4 = text_4.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 150))

            screen.blit(text, place)
            screen.blit(text_2, place_2)
            screen.blit(text_3, place_3)
            screen.blit(text_4, place_4)

            x_1, y_1 = pygame.mouse.get_pos()
            x_2, y_2 = pygame.mouse.get_pos()
            

            if x_1 >= WIDTH // 2 + 100 and x_1 <= 550 and y_1 >= 400 and y_1 <= 500:
                text_4 = font.render("НЕТ", True, (0, 200, 200))
                place_4 = text_4.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 150))
                screen.blit(text_4, place_4)
            elif x_2 <= WIDTH // 2 - 150 and x_2 >= 60 and y_2 >= 400 and y_2 <= 500:
                text_3 = font.render("ДА", True, (0, 200, 200))
                place_3 = text_3.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2  + 150))
                screen.blit(text_3, place_3)
            
            

    draw_grid()

    pygame.display.flip()
