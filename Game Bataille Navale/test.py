from asyncio import events
import sys
import pygame
from win32api import GetSystemMetrics

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
FPS = 60
pygame.init()
pygame.font.init()
pygame.mixer.init()

width, height = GetSystemMetrics(0), GetSystemMetrics(1)
window = pygame.display.set_mode((width, height-80))
pygame.display.set_caption("BATAILLE NAVIRE")

bg_img = pygame.image.load("Assets/bg-accueil.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height-80))

class Button:
    def __init__(self, text, pos):
        self.text = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont("comicsans", 100)
        self.change(WHITE, BLACK)
    
    def change(self, color, bg):
        self.bg = bg
        self.new_text = self.font.render(self.text, 1, pygame.Color(color))
        self.size = self.new_text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.new_text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def draw(self):
        window.blit(self.surface, (self.x, self.y))
        self.hover()
    
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    return True
                else:
                    return False

    def hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.change(RED, YELLOW)
        else:
            self.change(WHITE, BLACK)
    

button2 = Button("TEST TEST TEST TEST", (300, 500))



def main_test():
    running = True
    while running:
        clock.tick(FPS)
        window.blit(bg_img, (0, 0))
        button2.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

    pygame.quit()


