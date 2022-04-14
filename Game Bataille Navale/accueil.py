import sys
import pygame
from win32api import GetSystemMetrics
import one_player_add


# set the color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# initialize the module
pygame.init()
pygame.font.init()
pygame.mixer.init()

# set the screen system
width, height = GetSystemMetrics(0), GetSystemMetrics(1)
window = pygame.display.set_mode((width, height-80))
pygame.display.set_caption("BATAILLE NAVIRE")

bg_img = pygame.image.load("Assets/bg-accueil.jpg")
bg_img = pygame.transform.scale(bg_img, (width, height-80))

# create the button class
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
    
# create the button
button1 = Button("One player", (300, 300))
button2 = Button("Two player", (300, 500))

# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        window.blit(bg_img, (0, 0))
        button1.draw()
        button2.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if button1.click(event):
                one_player_add.main()

