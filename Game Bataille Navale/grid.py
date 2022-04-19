import sys
import pygame
from win32api import GetSystemMetrics
import random

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


# button Square

class Square:
    def __init__(self, size, pos):
        self.x, self.y = pos
        self.size = size
        self.change(BLACK)

    
    def change(self, color):
        self.color = color
        self.surface = pygame.Surface(self.size)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])  

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        self.hover()
    
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change(RED)

    def hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.change(YELLOW)
        else:
            self.change(BLACK)

# create a list for grid

def listGrid(size, prop):
    grid = []
    for i in range(size):
        line = []
        for j in range(size):
            if random.random() < prop:
                k = 1
            else:
                k = 0
            line.append(k)
        grid.append(line)
    return grid

# create the grid

class Grid:
    def __init__(self, size, pos):
        self.size = size
        self.x, self.y = pos
        self.blockSize = 30
        self.width = self.x + (self.blockSize*size)
        self.height = self.y + (self.blockSize*size)

        self.grid = listGrid(self.size, 0.5)


        self.list = []

        vertical = self.y
        i = 0
        while vertical < self.height:
            horizontal = self.x
            j = 0
            while horizontal < self.width:
                if self.grid[i][j] == 1:
                    target = True
                else:
                    target = False
                self.square = Square((self.blockSize, self.blockSize), (horizontal, vertical))
                self.list.append(self.square)
                horizontal += (self.blockSize + 2)
                j += 1
            vertical += (self.blockSize + 12)
            i += 1


    def draw(self):
        for i in self.list:
            i.draw()
    
    def click(self, event):
        self.event = event
        for i in self.list:
            i.click(self.event)





                
grid1 = Grid(15, (200, 200))



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
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            grid1.click(event)

main()


