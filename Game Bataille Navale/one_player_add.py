import sys
import pygame
from win32api import GetSystemMetrics


# set the color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
COLOR_INACTIVE_BOX = WHITE
COLOR_ACTIVE_BOX = RED
# initialize the modules
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
"""class Button:
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
            self.change(WHITE, BLACK)"""



# create the input box class
class Input_box:
    def __init__(self, size, pos):
        self.user_text = ""
        self.active = False
        self.color = COLOR_INACTIVE_BOX
        self.x, self.y = pos
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])
        self.font = pygame.font.Font(None, 60)
        self.text_surface = self.font.render(self.user_text, True, BLACK)
    
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        self.rect.w = max(100, self.text_surface.get_width()+10)

    def handle_event(self, event):
        self.event = event
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.active = True
                else:
                    self.active = False
                self.color = COLOR_ACTIVE_BOX if self.active else COLOR_INACTIVE_BOX
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            else:
                self.user_text += event.unicode
            self.text_surface = self.font.render(self.user_text, True, BLACK)   

         
# create the name input box
input1 = Input_box((600, 100), (300, 300))


# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        window.blit(bg_img, (0, 0))
        input1.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            input1.handle_event(event)

main()


