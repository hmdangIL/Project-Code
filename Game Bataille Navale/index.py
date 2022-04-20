import sys
import pygame
from win32api import GetSystemMetrics

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


# set the color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_INACTIVE_BOX = WHITE
COLOR_ACTIVE_BOX = RED






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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    return True
                else:
                    return False

    def hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.change(RED, YELLOW)
        else:
            self.change(WHITE, BLACK)


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
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


class Ship:
    def __init__(self, size, pos):
        self.draging = False
        self.size = size
        self.x, self.y = pos
        self.color = GREEN
    
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])  
        pygame.draw.rect(window, self.color, self.rect)
    
    def drag_drop(self, event):
        self.event = event
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_x, mouse_y):
                if event.button == 1:
                    self.draging = True
                    self.offset_x = self.x - mouse_x
                    self.offset_y = self.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.draging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.draging:
                mouse_x, mouse_y = event.pos
                self.x = mouse_x + self.offset_x
                self.y = mouse_y + self.offset_y


# button Square

class Square(Ship):
    def __init__(self, size, pos, listShip):
        self.listShip = listShip
        self.confirmed = False
        self.target = False
        self.hovered = False
        self.chose = False
        self.attacked = False
        self.color = BLACK
        self.x, self.y = pos
        self.size = size

        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])  
    
    def handle_event(self, event):
        self.event = event
        for ship in self.listShip:
            if self.rect.colliderect(ship.rect):
                self.hovered = True
                if (not ship.draging):
                    self.chose = True
                break
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

    def attack(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(mouse_x, mouse_y):
                    self.attacked = True
        if self.attacked:
            if self.target:
                self.color = BLUE
            else:
                self.color = WHITE     

    # def confirm_target(self, event):
        # self.confirmed = True


    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)


# create the grid

class Grid:
    def __init__(self, size, pos, listShip):
        self.listShip = listShip
        self.size = size
        self.x, self.y = pos
        self.blockSize = 35
        self.width = self.x + (self.blockSize*size)
        self.height = self.y + (self.blockSize*size)

        self.listSquare = []

        vertical = self.y
        i = 0
        while vertical < self.height:
            horizontal = self.x
            j = 0
            while horizontal < self.width:
                self.square = Square((self.blockSize, self.blockSize), (horizontal, vertical), self.listShip)
                self.listSquare.append(self.square)
                horizontal += (self.blockSize + 2)
                j += 1
            vertical += (self.blockSize + 12)
            i += 1

    def draw(self):
        for i in self.listSquare:
            i.draw()
    
    def handle_event(self, event):
        self.event = event
        for i in self.listSquare:
            i.handle_event(self.event)
    
    def attack(self, event):
        self.event = event
        for i in self.listSquare:
            i.attack(self.event)

    """def confirm_target(self, event):
        self.event = event
        for i in self.listSquare:
            i.confirm_target(self.event)"""