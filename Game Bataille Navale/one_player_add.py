import sys
import pygame
from win32api import GetSystemMetrics
import index



# create the name input box
input1 = index.Input_box((600, 100), (300, 300))


# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

# create the main function
def main():
    running = True
    while running:
        clock.tick(FPS)
        index.window.blit(index.bg_img, (0, 0))
        input1.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            input1.handle_event(event)



