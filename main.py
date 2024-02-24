from os import system
from random import choice

class Player:
    def __init__(self, is_automatic=True, image="X", is_center=False, is_predict=False):
        self.image = image
        self.is_automatic = is_automatic
        self.is_center = is_center
        self.is_predict = is_predict

    def get_winner(self) -> str:
        for i in range(0, 7, 3):
            if self.field.cells[i] == self.field.cells[i + 1] == self.field.cells[i + 2]:
                return self.field.cells[i]

        for i in range(3):
            if self.field.cells[i] == self.field.cells[i + 3] == self.field.cells[i + 2]:
                return self.field.cells[i]
            
        if self.field.cells[0] == self.field.cells[4] == self.field.cells[8]:
            return self.field.cells[i]
        
        if self.field.cells[2] == self.field.cells[4] == self.field.cells[6]:
            return self.field.cells[i]
        return ''

    
    def make_move(self, field):
        if not self.is_automatic:
            while True:
                try:
                    cell_number = int(input(f'введи номер клетки хода для {self.image}:'))
                except ValueError:
                    print("Ошибка! Номер клетки должен быть целым числом!")
                    continue
                if cell_number < 1 or cell_number > 9:
                    print("Ошибка! Номер клетки должен быть от 1 до 9 включительно!")
                    continue
                index = cell_number - 1
                if not isinstance(field.cells[index], int) :
                    print("Ошибка! Клетка занята!")
                    continue
                break
            field.cells[index] = self.image
        else:
            free_cells_indexes = []
            for i in range(9):
                if isinstance(field.cells[i], int):
                    free_cells_indexes.append(i)
            if self.is_center and 4 in free_cells_indexes:
                field.cells[4] = self.image
                return
            if self.is_predict:
                for index in free_cells_indexes:
                    field.cells[index] = self.image
                    if get_winner:
                        return
                    field.cells[index] = index + 1
            random_index = choice(free_cells_indexes)
            field.cells[random_index] = self.image


class Field:
    def __init__(self):
        self.cells = [i for i in range(1, 10)]

    def draw(self):
        system("cls")
        for i in range(0, 9, 3):
            print(self.cells[i], self.cells[i + 1], self.cells[i + 2])

class Game:
    def __init__(self, is_silent=False):
        self.pl_1 = Player(image="X", is_automatic=False, is_center=False, is_predict=False)
        self.pl_2 = Player(image="O", is_automatic=False, is_center=True, is_predict=True)
        self.field = Field()
        self.winner = None
        self.is_silent = is_silent

    def run(self):
        turn = 1
        while True:
            if turn > 9:
                print('Ничья!')
                break
            self.field.draw()
            if turn % 2: # Нечетный ход
                self.pl_1.make_move(self.field)
            else: # Четный ход
                self.pl_2.make_move(self.field)
            turn += 1
            self.winner = self.get_winner()
            if self.winner:
                print(f'Победил {self.winner}')
                break



class App:
    def __init__(self):
        self.statistics = [0, 0, 0] # x, o, ничья
        self.game = Game(True)
        self.game.run()
        if self.game.winner == 'X':
            self.statistics[0] += 1
        elif self.game.winner == 'O':
            self.statistics[1] += 1
        else:
            self.statistics[2] += 1
        print(*self.statistics)


App()

"""class Field:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        run = True
        while run:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                elif i.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


            pygame.display.update()"""
