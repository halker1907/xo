from os import system
from random import choices
import pygame
import sys



class Field:
    def __init__(self, screen):
        self.cells = [i for i in range(1, 10)]
        self.screen = screen
        

    def draw(self):
        system("cls")
        



class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.is_running = True
        


    def run(self):
        while self.is_running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.line(self.screen, (255, 255, 255), [[90, 0], [290, 0]], [90, 0], 9)
        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Window()
    game.run()
    game.quit_game()