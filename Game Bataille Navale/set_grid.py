import sys
import pygame
from win32api import GetSystemMetrics
import random

# set the color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
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



class Ship:
    def __init__(self, size, pos):
        Ship.draging = False
        self.size = size
        self.x, self.y = pos
        self.color = GREEN
    
    def draw(self):
        Ship.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])  
        pygame.draw.rect(window, self.color, Ship.rect)
    
    def drag_drop(self, event):
        self.event = event
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Ship.rect.collidepoint(mouse_x, mouse_y):
                if event.button == 1:
                    Ship.draging = True
                    self.offset_x = self.x - mouse_x
                    self.offset_y = self.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Ship.draging = False
        elif event.type == pygame.MOUSEMOTION:
            if Ship.draging:
                mouse_x, mouse_y = event.pos
                self.x = mouse_x + self.offset_x
                self.y = mouse_y + self.offset_y


# button Square

class Square(Ship):
    def __init__(self, size, pos):
        self.target = False
        self.hovered = False
        self.chose = False
        self.color = BLACK
        self.x, self.y = pos
        self.size = size

        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])  
    
    def handle_event(self, event):
        self.event = event
        if self.rect.colliderect(Ship.rect):
            self.hovered = True
            if (not Ship.draging):
                self.chose = True
        else:
            self.hovered = False
            self.chose = False
        if self.chose:
            self.target = True
            self.color = RED
        elif self.hovered:
            self.target = False
            self.color = YELLOW
        else:
            self.target = False
            self.color = BLACK

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


# create the grid

class Grid:
    def __init__(self, size, pos):
        self.size = size
        self.x, self.y = pos
        self.blockSize = 35
        self.width = self.x + (self.blockSize*size)
        self.height = self.y + (self.blockSize*size)

        self.list = []

        vertical = self.y
        i = 0
        while vertical < self.height:
            horizontal = self.x
            j = 0
            while horizontal < self.width:
                self.square = Square((self.blockSize, self.blockSize), (horizontal, vertical))
                self.list.append(self.square)
                horizontal += (self.blockSize + 2)
                j += 1
            vertical += (self.blockSize + 12)
            i += 1

    def draw(self):
        for i in self.list:
            i.draw()
    
    def handle_event(self, event):
        self.event = event
        for i in self.list:
            i.handle_event(self.event)








ship1 = Ship((30, 120), (1500, 300))
ship2 = Ship((30, 120), (1700, 300))









                
grid1 = Grid(15, (200, 250))



# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        window.blit(bg_img, (0, 0))
        grid1.draw()
        ship1.draw()
        ship2.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            grid1.handle_event(event)
            ship1.drag_drop(event)
            ship2.drag_drop(event)

main()


