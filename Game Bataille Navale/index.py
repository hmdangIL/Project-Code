import sys
import pygame
from win32api import GetSystemMetrics
import random

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

# set the size of grid
SIZE_GRID_SMALL = 7
SIZE_GRID_MEDIUM = 10






# create the button class
class Button:
    def __init__(self, text, pos, size):
        self.size = size
        self.text = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont("comicsans", self.size)
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
        self.size_x = size[0]
        self.size_y = size[1]
        self.x, self.y = pos
        self.color = GREEN
    
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.size_x, self.size_y)  
        pygame.draw.rect(window, self.color, self.rect)
    
    def handle_event(self, event):
        # drag and drop
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
        # rotate
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(mouse_x, mouse_y):
                if event.button == 3:
                    a = self.size_x
                    self.size_x = self.size_y
                    self.size_y = a

    """def reset(self):
        self.draging = False
        self.size_x = size[0]
        self.size_y = size[1]
        self.x, self.y = pos
        self.color = GREEN"""


# button Square

class Square(Ship):
    def __init__(self, size, pos, listShip, dataTarget):
        self.isChangeTurn = False
        self.listShip = listShip
        self.dataTarget = dataTarget
        # self.confirmed = False
        if dataTarget == 0:
            self.target = False
        elif dataTarget == 1:
            self.target = True
        self.hovered = False
        self.chose = False
        self.isAttacked = False
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

    def attacked(self, event):
        if self.isOnAttacked:
            self.event = event
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if self.rect.collidepoint(mouse_x, mouse_y):
                        if not self.isAttacked:
                            if not self.target:
                                self.isChangeTurn = True
                            self.isAttacked = True
        if self.isAttacked:
            if self.target:
                self.color = BLUE
            else:
                self.color = WHITE
            
    
    def isTarget(self):
        if self.target:
            return True
        else:
            return False
    
    def isKilled(self):
        self.isAttacked = True
        if not self.target:
            self.isChangeTurn = True
    


    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

    def dead(self):
        if self.isAttacked:
            return True
        else:
            return False
    
    def onAttacked(self):
        self.isOnAttacked = True
    
    def offAttacked(self):
        self.isOnAttacked = False
    
    def resetTurn(self):
        self.isChangeTurn = False
    
    def changeTurn(self):
        return self.isChangeTurn



# create the grid

class Grid:
    def __init__(self, size, pos, listShip=[], getData=False):
        self.turnAttacked = False
        self.listShip = listShip
        self.size = size
        self.getData = getData
        if self.getData == True:
            self.dataTarget = self.findGridDataPlayer1()
        elif self.getData == False:
            self.dataTarget = []
            for i in range(self.size * self.size):
                self.dataTarget.append(0)
        elif self.getData == "Random":
            self.dataTarget = gridDataRandom(SIZE_GRID_MEDIUM)



        self.x, self.y = pos
        self.blockSize = 35
        self.width = self.x + (self.blockSize*size) + (self.size-1)*5
        self.height = self.y + (self.blockSize*size) + (self.size-1)*5

        self.listSquare = []

        vertical = self.y
        i = 0
        self.indexDataTarget = 0
        while vertical < self.height:
            horizontal = self.x
            j = 0
            while horizontal < self.width:
                self.square = Square((self.blockSize, self.blockSize), (horizontal, vertical), self.listShip, self.dataTarget[self.indexDataTarget])
                self.listSquare.append(self.square)
                self.indexDataTarget += 1
                horizontal += (self.blockSize + 5)
                j += 1
            vertical += (self.blockSize + 5)
            i += 1

    def draw(self):
        for i in self.listSquare:
            i.draw()
    
    def handle_event(self, event):
        self.event = event
        for i in self.listSquare:
            i.handle_event(self.event)
    
    def attacked(self, event):
        self.event = event
        for i in self.listSquare:
            i.attacked(self.event)
        
    
    def save(self, file_path):
        with open(file_path, 'w') as data:
            for i in self.listSquare:
                if i.isTarget():
                    data.write(str(1) + '\n')
                else:
                    data.write(str(0) + '\n')

    def findGridDataPlayer1(self):
        gridData = open('gridDataPlayer1.txt')
        data = []
        for line in gridData:
            data.append(int(line[:-1]))
        gridData.close()
        return data
    
    def onAttacked(self):
        for i in self.listSquare:
            i.onAttacked()

    
    def offAttacked(self):
        for i in self.listSquare:
            i.offAttacked()


    def randomAttacked(self):
        i = random.choice(self.listSquare)
        while i.dead():
            i = random.choice(self.listSquare)
        i.isKilled()
    
    def countTarget(self):
        self.target = 0
        for i in self.listSquare:
            if i.isTarget():
                self.target += 1
        return self.target
    
    def countTargetAlive(self):
        self.targetAlive = 0
        for i in self.listSquare:
            if (i.isTarget()) and (not i.dead()):
                self.targetAlive += 1
        return self.targetAlive

    def changeTurn(self):
        self.isChangeTurn = False
        for i in self.listSquare:
            if i.changeTurn():
                self.isChangeTurn = True
        return self.isChangeTurn
    
    def resetTurn(self):
        for i in self.listSquare:
            i.resetTurn()
    
    """def reset(self):
        self.turnAttacked = False
        self.listShip = listShip
        self.size = size
        self.getData = getData
        if self.getData == True:
            self.dataTarget = self.findGridDataPlayer1()
        elif self.getData == False:
            self.dataTarget = []
            for i in range(self.size * self.size):
                self.dataTarget.append(0)
        elif self.getData == "Random":
            self.dataTarget = gridDataRandom(SIZE_GRID_MEDIUM)"""




def gridDataRandom(size):
    dataTarget = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        dataTarget.append(line)
    listTargetChose = []



    if size == SIZE_GRID_SMALL:
        # 1 shipM and 5 shipS

        # 1 shipM
        shipM_Added = 0
        while shipM_Added < 1:
            yShipM = random.randint(0, size-1)
            if yShipM > (size-3):
                xShipM = random.randint(0, size-3)
                horizontal = True
            else:
                horizontal = random.choice([True, False])
                if horizontal:
                    xShipM = random.randint(0, size-3)
                else:
                    xShipM = random.randint(0, size-1)
            
            if horizontal:
                canAdded = True
                for i in range(xShipM, xShipM+3):
                    if (yShipM, i) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(xShipM, xShipM+3):
                        dataTarget[yShipM][i] = 1
                        listTargetChose.append((yShipM, i))
                    shipM_Added += 1
            else:
                canAdded = True
                for i in range(yShipM, yShipM+3):
                    if (i, xShipM) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(yShipM, yShipM+3):
                        dataTarget[i][xShipL] = 1
                        listTargetChose.append((i, xShipL))
                    shipM_Added += 1      

        # 5 shipS
        shipS_Added = 0
        while shipS_Added < 5:
            xShipS = random.randint(0, 6)
            yShipS = random.randint(0, 6)
            if (yShipS, xShipS) not in listTargetChose:
                dataTarget[yShipS][xShipS] = 1
                shipS_Added += 1
                listTargetChose.append((yShipS, xShipS))


    if size == SIZE_GRID_MEDIUM:
        # 1 shipL and 2 shipM and 5 shipS

        # 1 shipL
        shipL_Added = 0
        while shipL_Added < 1:
            yShipL = random.randint(0, size-1)
            if yShipL > (size-5):
                xShipL = random.randint(0, size-5)
                horizontal = True
            else:
                horizontal = random.choice([True, False])
                if horizontal:
                    xShipL = random.randint(0, size-5)
                else:
                    xShipL = random.randint(0, size-1)
            
            if horizontal:
                canAdded = True
                for i in range(xShipL, xShipL+5):
                    if (yShipL, i) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(xShipL, xShipL+5):
                        dataTarget[yShipL][i] = 1
                        listTargetChose.append((yShipL, i))
                    shipL_Added += 1
            else:
                canAdded = True
                for i in range(yShipL, yShipL+5):
                    if (i, xShipL) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(yShipL, yShipL+5):
                        dataTarget[i][xShipL] = 1
                        listTargetChose.append((i, xShipL))
                    shipL_Added += 1


        
        # 2 shipM
        shipM_Added = 0
        while shipM_Added < 2:
            yShipM = random.randint(0, size-1)
            if yShipM > (size-3):
                xShipM = random.randint(0, size-3)
                horizontal = True
            else:
                horizontal = random.choice([True, False])
                if horizontal:
                    xShipM = random.randint(0, size-3)
                else:
                    xShipM = random.randint(0, size-1)
            
            if horizontal:
                canAdded = True
                for i in range(xShipM, xShipM+3):
                    if (yShipM, i) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(xShipM, xShipM+3):
                        dataTarget[yShipM][i] = 1
                        listTargetChose.append((yShipM, i))
                    shipM_Added += 1
            else:
                canAdded = True
                for i in range(yShipM, yShipM+3):
                    if (i, xShipM) in listTargetChose:
                        canAdded = False
                if canAdded:
                    for i in range(yShipM, yShipM+3):
                        dataTarget[i][xShipM] = 1
                        listTargetChose.append((i, xShipM))
                    shipM_Added += 1

        
        # 5 shipS
        shipS_Added = 0
        while shipS_Added < 5:
            xShipS = random.randint(0, 6)
            yShipS = random.randint(0, 6)
            if (yShipS, xShipS) not in listTargetChose:
                dataTarget[yShipS][xShipS] = 1
                listTargetChose.append((yShipS, xShipS))
                shipS_Added += 1

    res = []
    for line in dataTarget:
        for data in line:
            res.append(data)

    return res
