from os import system

class Player:
    def __init__(self, is_automatic=True, image="X"):
        self.image = image
        self.is_automatic = is_automatic
    
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


class Field:
    def __init__(self):
        self.cells = [i for i in range(1, 10)]

    def draw(self):
        system("cls")
        for i in range(0, 9, 3):
            print(self.cells[i], self.cells[i + 1], self.cells[i + 2])

class Game:
    def __init__(self):
        self.pl_1 = Player(image="X", is_automatic=False)
        self.pl_2 = Player(image="O", is_automatic=False)
        self.field = Field()

    def run(self):
        #начинаем с первого хода
        while True: #выйти на 10 ходу - ничья
            self.field.draw()
            if :#нечетный ход
                self.pl_1.make_move(self.field)
            else:#четный ход
                self.pl_2.make_move(self.field)
            #добавляем к ходам + 1
            #проверить победителя



class App:
    def __init__(self):
        self.game = Game()
        self.game.run()


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
